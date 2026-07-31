"""
Regenerate the three PNG charts used in the deck and one-pager.

Outputs to /workspace/business-case-repo/charts/:
  - profit_vs_price.png    (slide 6 + one-pager header)
  - breakeven_vs_price.png (deck appendix)
  - sensitivity.png        (slide 7 — the risk slide)

Run:
    python3 make_chart.py
"""

import os
import sys
import matplotlib.pyplot as plt
import numpy as np

# Make the model importable regardless of where this script is run from
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from model import profit_at, breakeven_at  # noqa: E402

OUT = os.path.join(os.path.dirname(HERE), "charts")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------
# Assumptions
# ---------------------------------------------------------------------------
V, F, T = 40, 3000, 25

TIERS = [(150, "Floor (£150)"),
         (200, "Base (£200)"),
         (250, "Premium (£250)"),
         (300, "Aspirational (£300)")]

# ---------------------------------------------------------------------------
# Chart 1 — Profit vs Price
# ---------------------------------------------------------------------------
def chart_profit():
    prices = np.arange(100, 351, 1)
    profits = [profit_at(p, V, F, T) for p in prices]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(prices, profits, color="#1f4e79", linewidth=2.5,
            label="Monthly profit (25 trolleys)")
    ax.axhline(0, color="grey", linestyle="--", linewidth=1, alpha=0.6)

    for p, label in TIERS:
        prof = profit_at(p, V, F, T)
        colour = "#b30000" if p == 200 else "#1f4e79"
        weight = "bold" if p == 200 else "normal"
        ax.scatter([p], [prof], s=90, color=colour, zorder=5)
        ax.annotate(f"£{p}\n£{prof:+,}",
                    xy=(p, prof), xytext=(0, 14), textcoords="offset points",
                    ha="center", fontsize=10, color=colour, fontweight=weight)

    ax.set_title("Riverside Malls — Smart Trolley Pilot\n"
                 "Profit vs Price (v=£40, F=£3,000, 25 trolleys)",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("Operator price per trolley per month (£)", fontsize=11)
    ax.set_ylabel("Monthly profit (£)", fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")
    ax.set_xlim(100, 350)

    out = os.path.join(OUT, "profit_vs_price.png")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  wrote {out}")


# ---------------------------------------------------------------------------
# Chart 2 — Break-even Trolleys vs Price
# ---------------------------------------------------------------------------
def chart_breakeven():
    prices = np.arange(100, 351, 1)
    bes = [breakeven_at(p, V, F) for p in prices]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(prices, bes, color="#2e7d32", linewidth=2.5,
            label="Break-even trolleys")
    ax.axhline(T, color="red", linestyle="--", linewidth=1.5,
               label="Pilot fleet size (25)")
    ax.fill_between(prices, T, max(bes) + 5, color="red", alpha=0.08,
                    label="Misses break-even zone")

    for p, label in TIERS:
        be = breakeven_at(p, V, F)
        colour = "#b30000" if p == 200 else "#1b5e20"
        weight = "bold" if p == 200 else "normal"
        ax.scatter([p], [be], s=90, color=colour, zorder=5)
        ax.annotate(f"{be:.1f}", xy=(p, be), xytext=(0, 12),
                    textcoords="offset points", ha="center",
                    fontsize=10, color=colour, fontweight=weight)

    ax.set_title("Break-even Trolleys vs Price\n"
                 "(Above 25 = pilot loses money)",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("Operator price per trolley per month (£)", fontsize=11)
    ax.set_ylabel("Trolleys needed to break even", fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")
    ax.set_xlim(100, 350)
    ax.set_ylim(5, 36)

    out = os.path.join(OUT, "breakeven_vs_price.png")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  wrote {out}")


# ---------------------------------------------------------------------------
# Chart 3 — Sensitivity
# ---------------------------------------------------------------------------
def chart_sensitivity():
    base = profit_at(200, V, F, T)                 # +£1,000
    stress_support = profit_at(200, V * 2, F, T)   # exactly £0
    churn = profit_at(200, V, F + 0.20 * T * 120, T * (1 - 0.20))  # -£400

    fig, ax = plt.subplots(figsize=(10, 5.5))
    labels = ["Baseline (v=£40)", "2× support (v=£80)", "20% monthly churn"]
    vals   = [base, stress_support, churn]
    colours = ["#2e7d32" if v >= 0 else "#b71c1c" for v in vals]
    bars = ax.bar(labels, vals, color=colours, width=0.55)

    for bar, v in zip(bars, vals):
        offset = 60 if v >= 0 else -90
        ax.text(bar.get_x() + bar.get_width() / 2, v + offset,
                f"£{v:+,.0f}", ha="center",
                fontsize=12, fontweight="bold", color="black")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Sensitivity: How much margin can we lose before the pilot breaks?",
                 fontsize=13, fontweight="bold")
    ax.set_ylabel("Monthly profit at £200/trolley (£)", fontsize=11)
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_ylim(-600, 1300)

    out = os.path.join(OUT, "sensitivity.png")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  wrote {out}")


if __name__ == "__main__":
    print("Regenerating charts...")
    chart_profit()
    chart_breakeven()
    chart_sensitivity()
    print("Done.")
