# BlueStock Mutual Fund Database

## Dataset Overview

This database contains cleaned mutual fund data used for financial analytics.

---

# Table: fact_nav

| Column | Data Type | Description |
|----------|-----------|-------------|
| date | DATE | NAV Date |
| amfi_code | INTEGER | Unique AMFI Code |
| nav | REAL | Net Asset Value |

---

# Table: fact_transactions

| Column | Data Type | Description |
|----------|-----------|-------------|
| investor_id | INTEGER | Investor Identifier |
| transaction_date | DATE | Date of Transaction |
| amfi_code | INTEGER | Mutual Fund Code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | Tier Classification |
| payment_mode | TEXT | UPI / NetBanking / Card etc. |
| kyc_status | TEXT | Verified / Pending |

---

# Table: fact_performance

| Column | Data Type | Description |
|----------|-----------|-------------|
| return_1yr_pct | REAL | 1-Year Return (%) |
| return_3yr_pct | REAL | 3-Year Return (%) |
| return_5yr_pct | REAL | 5-Year Return (%) |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Alpha Ratio |
| beta | REAL | Beta Ratio |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| expense_ratio_pct | REAL | Expense Ratio (%) |
| morningstar_rating | INTEGER | Rating (1–5) |
| risk_grade | TEXT | Risk Category |