# Riverside Malls — Smart Trolley Pilot · Business-Case Repo

> **Recommendation:** Run the pilot. Charge **£200 per trolley per month**.
> Monthly profit: **£1,000** · Break-even: **18.75 trolleys** · Margin of safety: **6.25 trolleys**.

This is the complete deliverable bundle for **Day 9 — Consulting Recommendation** of the
Knull Work Experience Programme. Every artefact can be regenerated from the Python
source in `src/`.

---

## The maths, in one line

```
monthly_profit  =  T × (P − v) − F
break_even_n*   =  F / (P − v)
```

With `T = 25`, `v = £40`, `F = £3,000`, `P = £200`:
- contribution = **£160**
- monthly profit = **£1,000**
- break-even = **18.75 trolleys** → 6.25 margin of safety

At `P = £150`: −£250/month, break-even = 27.3 trolleys (misses).
At `P = £250`: +£2,250/month, break-even = 14.3 trolleys.

---

## File map

| # | Deliverable | File | Open this if you want to… |
|---|---|---|---|
| 1 | **Unit-economics model** (Python) | `src/model.py` | see the formula in code · run `python3 src/model.py` |
| 2 | **Profit-vs-price chart** | `charts/profit_vs_price.png` | see the headline curve · `python3 src/make_chart.py` |
| 3 | **Break-even curve** | `charts/breakeven_vs_price.png` | see where each price tier breaks · same script |
| 4 | **Sensitivity chart** | `charts/sensitivity.png` | see the stress test · same script |
| 5 | **Live-formula Excel model** | `unit_economics.xlsx` | change a number on `Assumptions` and watch everything update · `python3 src/build_xlsx.py` |
| 6 | **Product one-pager** | `one_pager.pdf` · `one_pager.html` | see the MVP scope and what's out |
| 7 | **Consulting deck (8 slides)** | `consulting_deck.pptx` · `consulting_deck.pdf` | see the full recommendation up front · `python3 src/build_deck.py` |
| 8 | **Reflection journal #9** | `docs/reflection_journal_09.md` | read what was learned |
| 9 | **Founder's memo (150 words)** | `docs/founders_memo.md` | read the "is this a business?" verdict |

---

## Directory layout

```
business-case-repo/
├── README.md                          ← you are here
├── model.py  ← (use src/model.py)     ← the 4-line model from Step 2
├── unit_economics.xlsx                ← live-formula workbook (4 sheets, 80 formulas)
├── consulting_deck.pptx               ← 8-slide deck
├── consulting_deck.pdf                ← same deck, PDF rendering
├── one_pager.html                     ← source for the one-pager
├── one_pager.pdf                      ← rendered one-pager
├── src/                               ← all Python source, regenerates everything
│   ├── model.py                       ← core unit_economics() function
│   ├── make_chart.py                  ← regenerates the 3 PNGs
│   ├── build_xlsx.py                  ← regenerates the Excel workbook
│   └── build_deck.py                  ← regenerates the PPTX deck
├── charts/                            ← the three PNGs
│   ├── profit_vs_price.png
│   ├── breakeven_vs_price.png
│   └── sensitivity.png
└── docs/
    ├── reflection_journal_09.md
    └── founders_memo.md
```

---

## How to reproduce everything from scratch

```bash
cd src
python3 model.py            # prints the price-tier table
python3 make_chart.py       # regenerates charts/profit_vs_price.png etc.
python3 build_xlsx.py       # regenerates ../unit_economics.xlsx
python3 build_deck.py       # regenerates ../consulting_deck.pptx
```

The one-pager is plain HTML — open `one_pager.html` in a browser, or use
`libreoffice --headless --convert-to pdf one_pager.html` for the PDF.

---

## What the submission page should see

If the form asks for a single zip / folder, attach this whole directory.
If it asks for individual files, attach at minimum:

1. **`src/model.py`** — the Python unit-economics model (matches the Step-2 spec)
2. **`unit_economics.xlsx`** — the live-formula version of the same model
3. **`consulting_deck.pptx`** *(or* `.pdf`*)* — the recommendation deck
4. **`one_pager.pdf`** — the product brief
5. **`docs/reflection_journal_09.md`** — journal entry #9
6. **`docs/founders_memo.md`** — the stretch founder's memo

---

## Definition of done — check

- [x] Unit-economics model testing 4 price tiers, with a profit-vs-price chart
- [x] Product one-pager (users, job, MVP, out-of-scope)
- [x] Consulting deck (8 slides) with a clear, numbers-backed recommendation
- [x] Reflection journal entry #9
- [x] Stretch: sensitivity analysis (2× support, 20% churn)
- [x] Stretch: 150-word founder's memo (149 words)

---

*Day 9 · Riverside Malls · Smart Trolley Pilot · Confidential to participants*
