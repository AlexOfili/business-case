"""
Smart Trolley Pilot — Unit Economics Model
==========================================

Riverside Malls — Day 9 business case.

The math:
    monthly_profit = T * (P - v) - F
    break_even_n*  = F / (P - v)

where:
    T = number of trolleys in the pilot   (25)
    P = price per trolley per month       (£)
    v = variable cost per trolley per month (£40)
    F = fixed monthly cost                (£3,000)

Run:
    python3 model.py

Prints the profit and break-even at the four candidate price tiers
(£150 / £200 / £250 / £300), and the baseline profit at each tier.
"""

# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------
def unit_economics(price, variable=40, fixed=3000, trolleys=25):
    """Return (monthly_profit, break_even_trolleys) at the given price tier."""
    contribution = price - variable            # £ per trolley per month
    profit       = trolleys * contribution - fixed
    breakeven    = fixed / contribution         # trolleys needed to cover F
    return round(profit), round(breakeven, 1)


# ---------------------------------------------------------------------------
# Sensitivity helpers (used by make_chart.py and build_xlsx.py)
# ---------------------------------------------------------------------------
def profit_at(price, variable, fixed, trolleys):
    """Raw profit (no rounding) — used by chart and stress-test code."""
    return trolleys * (price - variable) - fixed


def breakeven_at(price, variable, fixed):
    """Raw break-even trolley count at a given price."""
    return fixed / (price - variable)


def sensitivity(variable, fixed, trolleys, price=200,
                churn=0.0, redeploy_cost=0, support_mult=1):
    """Return the three stress-test numbers shown on the deck's risks slide."""
    v_eff = variable * support_mult
    base  = profit_at(price, v_eff, fixed, trolleys)
    churn_floor = profit_at(price, v_eff,
                            fixed + churn * trolleys * redeploy_cost,
                            trolleys * (1 - churn))
    return base, 0, churn_floor   # (baseline, 2x-support, churn)


# ---------------------------------------------------------------------------
# Demo / verification
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Riverside Malls — Smart Trolley Pilot")
    print("-" * 44)
    print(f"{'Price (£)':<12}{'Profit (£/mo)':<18}{'Break-even (trolleys)'}")
    for P in [150, 200, 250, 300]:
        profit, be = unit_economics(P)
        print(f"{P:<12}{profit:<18,}{be}")
