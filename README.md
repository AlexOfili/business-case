# Riverside Malls — Smart Trolley Pilot

> **Recommendation:** Run the pilot. Charge **£200 per trolley per month**.
> Monthly profit: **£1,000** · Break-even: **18.75 trolleys** · Margin of safety: **6.25 trolleys**.

## How to run `model.py`

The whole model is a single 4-line function plus a 4-line loop. Nothing to install.

```bash
python3 model.py
```

Expected output:

```
Riverside Malls — Smart Trolley Pilot
--------------------------------------------
Price (£)   Profit (£/mo)     Break-even (trolleys)
150         -250              27.3
200         1,000             18.8
250         2,250             14.3
300         3,500             11.5
```

## What `model.py` does, and how

It computes two things at each candidate price:

- **Monthly profit** — the cash the pilot makes (or loses) per month
- **Break-even trolley count** — the smallest fleet size that covers the fixed cost

The math:

```
monthly_profit  =  T × (P − v) − F
break_even_n*   =  F / (P − v)
```

Where:

| Symbol | Meaning                          | Value |
|--------|----------------------------------|-------|
| `T`    | number of trolleys in the pilot  | 25    |
| `P`    | price per trolley per month (£)  | varies |
| `v`    | variable cost per trolley (£)    | 40    |
| `F`    | fixed monthly cost (£)           | 3,000 |

Read across the row: at the £200 base tier, the pilot makes £1,000/month and breaks even at 18.75 trolleys — so the 25-trolley fleet has a 6.25-trolley margin of safety.



