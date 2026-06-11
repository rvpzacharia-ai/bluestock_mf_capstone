# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project analyzes Indian mutual fund data using Python, Pandas, SQL, and SQLite. The goal is to build a complete data pipeline from raw data ingestion to data cleaning, database design, SQL analytics, and dashboard-ready datasets.

## Project Objectives

* Collect and validate mutual fund datasets
* Clean and standardize financial data
* Build a SQLite analytics database
* Perform SQL-based analysis
* Generate insights on fund performance, NAV trends, SIP inflows, AUM, and investor transactions

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

Additional live NAV data was fetched from MFAPI for selected mutual fund schemes.

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── scripts/
├── sql/
├── reports/
├── dashboard/
├── notebooks/
├── requirements.txt
└── README.md
```

---

## Day 1 Deliverables

* Project setup and folder structure
* Data ingestion using Pandas
* Data quality checks
* AMFI code validation
* Fund master exploration
* Live NAV API integration
* Data quality summary report

---

## Day 2 Deliverables

* Cleaned and validated datasets
* Processed CSV files generated
* SQLite database created
* Star schema design
* SQL analytical queries
* Row count validation
* Data dictionary documentation

---

## Day 3 Deliverables

### Exploratory Data Analysis (EDA)

The third phase of the project focused on analyzing mutual fund industry trends and investor behavior through data visualization and exploratory analytics.

### Completed Analyses

* NAV Trend Analysis (2022–2026) with market event highlighting
* AUM Growth Analysis by Fund House
* SIP Inflow Trend Analysis
* Category-wise Inflow Heatmap
* Investor Demographics Analysis

  * Age Group Distribution
  * Gender Distribution
  * Investment Amount Analysis
* Geographic Distribution Analysis

  * State-wise SIP Contribution
  * T30 vs B30 Investor Distribution
* Folio Count Growth Analysis
* NAV Return Correlation Matrix
* Sector Allocation Analysis using Portfolio Holdings
* Documentation of 10 Key EDA Insights

### Visualizations Generated

* 15+ analytical charts and dashboards
* Interactive Plotly visualizations
* Seaborn statistical visualizations
* Matplotlib-based analytical charts
* Export-ready chart files for reporting

## Day 4 – Fund Performance Analytics

Completed:

- Daily Return Calculation
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta Analysis
- Maximum Drawdown Analysis
- Fund Scorecard Generation
- Benchmark Comparison
- Tracking Error Analysis

Outputs:
- fund_scorecard.csv
- alpha_beta.csv
- benchmark_comparison.png


---

## Day 5 – Interactive Dashboard Development

### Completed:

- Connected Power BI to all cleaned mutual fund datasets
- Created data model relationships using AMFI Code and Date fields
- Built Industry Overview dashboard with KPI cards, AUM trend analysis, and AMC-wise AUM comparison
- Built Fund Performance dashboard with risk-return scatter plot, scorecard table, NAV trend analysis, and interactive slicers
- Built Investor Analytics dashboard with state-wise investments, transaction distribution, age-group analysis, and monthly transaction trends
- Built SIP & Market Trends dashboard with SIP inflow analysis, benchmark trend tracking, category inflow heatmap, and top inflow categories
- Implemented drill-through navigation from Fund Performance to NAV Detail page
- Added interactive filters and dashboard navigation
- Exported dashboard as Power BI report, PDF report, and PNG screenshots

### Outputs:

- bluestock_mf_dashboard.pbix
- Dashboard.pdf
- Industry_Overview.png
- Fund_Performance.png
- Investor_Analytics.png
- SIP_Market_Trends.png

---

## Day 6 – Advanced Analytics & Risk Metrics

### Completed:

- Historical Value at Risk (VaR 95%) analysis for all mutual fund schemes
- Conditional Value at Risk (CVaR) calculation for downside risk assessment
- Rolling 90-Day Sharpe Ratio computation and trend analysis
- Investor Cohort Analysis based on first transaction year
- SIP Continuity Analysis and identification of at-risk investors
- Rule-based Mutual Fund Recommendation System based on risk appetite
- Sector Concentration Analysis using Herfindahl-Hirschman Index (HHI)
- Generated advanced investment and risk insights

### Outputs:

- Advanced_Analytics.ipynb
- var_cvar_report.csv
- recommender.py
- rolling_sharpe_chart.png

---
## Status

✅ Day 1 Completed

✅ Day 2 Completed

✅ Day 3 Completed

✅ Day 4 Completed

✅ Day 5 Completed

✅ Day 6 Completed

🚀 Final Report & Presentation Remaining
