# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Name of mutual fund scheme |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| sub_category | TEXT | Detailed category |
| risk_category | TEXT | Risk level |

---

## 02_nav_history.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1-year return |
| return_3yr_pct | REAL | 3-year return |
| return_5yr_pct | REAL | 5-year return |
| expense_ratio_pct | REAL | Expense ratio percentage |

---

## 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|----------|----------|
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| kyc_status | TEXT | KYC verification status |

Source:
Bluestock Mutual Fund Analytics Capstone Dataset