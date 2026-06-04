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

### Deliverables

* EDA_Analysis.ipynb
* 15+ visualizations
* Exported PNG charts
* Interactive Plotly HTML visualizations
* Business insights documentation

---

## Key Technologies

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Jupyter Notebook
* Plotly
* Matplotlib
* Seaborn

---

## Outputs

* 10 cleaned datasets
* SQLite database (`bluestock_mf.db`)
* SQL schema
* Analytical SQL queries
* Data quality reports
* Data dictionary
* EDA_Analysis.ipynb
* 15+ visualizations
* Exported PNG charts
* Interactive Plotly visualizations
* Business insights documentation

---

## Status

✅ Day 1 Completed

✅ Day 2 Completed

✅ Day 3 Completed (EDA & Visualization)
