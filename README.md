\# Bluestock MF Capstone



\## Day 1 — Data Quality \& Anomaly Report



\### 1. Null Values

\- \*\*File:\*\* `04\_monthly\_sip\_inflows.csv`

\- \*\*Column:\*\* `yoy\_growth\_pct` — 12 NULLs (expected: no prior-year data for first 12 months)

\- \*\*Action:\*\* Leave as NaN; handle downstream in analysis



\### 2. Incorrect dtypes

\- \*\*Files:\*\* 01, 02, 03, 04, 05, 06, 08, 09, 10

\- \*\*Issue:\*\* Date columns (`date`, `month`, `launch\_date`, `transaction\_date`, `portfolio\_date`) read as `object` instead of `datetime64`

\- \*\*Action:\*\* Apply `pd.to\_datetime()` during Day 2 processing



\### 3. Pandas Deprecation Warning

\- \*\*Cause:\*\* `select\_dtypes(include="object")` triggers `Pandas4Warning`

\- \*\*Action:\*\* Replace with `include="string"` in Day 2 refactor



\### 4. Duplicate Rows

\- \*\*Status:\*\* None detected across all 10 files ✅

