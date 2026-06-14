# Bluestock Mutual Fund Analytics Capstone

## Overview

The **Bluestock Mutual Fund Analytics Capstone** is an end-to-end data engineering, analytics, and business intelligence project focused on the Indian Mutual Fund industry. The project demonstrates the complete lifecycle of financial data processing, including data ingestion, cleaning, transformation, database design, SQL analytics, performance evaluation, risk analysis, and dashboard development.

Using Python, Pandas, SQLite, SQL, and Power BI, the project converts raw mutual fund datasets into actionable insights for investors, analysts, and fund managers.

---

## Business Problem

Mutual fund data is distributed across multiple sources and formats, making it difficult to perform integrated analysis of fund performance, investor behavior, SIP trends, and industry growth.

This project addresses these challenges by building a centralized analytics platform capable of:

* Consolidating mutual fund datasets
* Automating ETL processes
* Performing financial and risk analytics
* Generating business insights
* Providing interactive dashboards for decision-making

---

## Project Objectives

* Collect and validate mutual fund datasets
* Build a scalable ETL pipeline
* Clean and standardize financial data
* Design a relational analytics database
* Perform SQL-based analytics
* Analyze mutual fund performance metrics
* Generate business and investment insights
* Build interactive Power BI dashboards

---

## Technology Stack

| Category        | Technologies                          |
| --------------- | ------------------------------------- |
| Programming     | Python                                |
| Data Processing | Pandas, NumPy                         |
| Database        | SQLite                                |
| Query Language  | SQL                                   |
| Visualization   | Power BI, Matplotlib, Seaborn, Plotly |
| Development     | Jupyter Notebook                      |
| Version Control | Git, GitHub                           |

---

# Project Architecture

Raw Data Sources
↓
Data Validation & Quality Checks
↓
Data Cleaning & Standardization
↓
SQLite Data Warehouse
↓
SQL Analytics Layer
↓
Performance & Risk Analysis
↓
Power BI Dashboard
↓
Business Insights & Recommendations

---

# Data Sources

The project integrates multiple mutual fund datasets covering industry, investor, and performance metrics.

### Datasets Used

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

### External Data Source

* MFAPI (Live NAV Data)

---

# Repository Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/                      # Original AMFI downloads
│   ├── processed/                # Cleaned datasets
│   └── db/
│       └── bluestock_mf.db       # SQLite database
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── amfi_validation.py
│   ├── check_db.py
│   ├── clean_nav_history.py
│   ├── clean_performance.py
│   ├── clean_transactions.py
│   ├── copy_remaining_files.py
│   ├── data_ingestion.py
│   ├── explore_fund_master.py
│   ├── explore_nav_history.py
│   ├── fund_master_analysis.py
│   ├── live_nav_fetch.py
│   ├── load_to_sqlite.py
│   ├── verify_counts.py
│   └── run_pipeline.py           # Master execution script
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── Mutual_Fund_Analytics.pbix
│
├── exports/
│   ├── charts/
│   ├── reports/
│   └── screenshots/
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ETL Pipeline

## Extract

* Import mutual fund datasets
* Fetch live NAV data from MFAPI
* Validate AMFI scheme codes

## Transform

* Handle missing values
* Standardize date formats
* Normalize financial metrics
* Remove duplicates
* Create derived performance indicators

## Load

* Store cleaned datasets
* Populate SQLite database
* Create analytical tables
* Prepare dashboard-ready datasets

---

# Day-wise Deliverables

## Day 1 – Data Collection & Validation

### Completed

* Project setup
* Folder structure creation
* Data ingestion using Pandas
* Data quality assessment
* AMFI code validation
* Live NAV API integration

### Outputs

* Raw datasets
* Data quality reports
* Validation logs

---

## Day 2 – Data Cleaning & Database Design

### Completed

* Data cleaning
* Missing value treatment
* Standardization
* SQLite database creation
* Star schema design
* SQL analytics setup

### Outputs

* Cleaned datasets
* SQLite database
* Data dictionary
* Validation reports

---

## Day 3 – Exploratory Data Analysis

### Completed

#### NAV Analysis

* NAV trends (2022–2026)
* Return distribution
* Correlation analysis

#### AUM Analysis

* AMC-wise growth
* Industry market share

#### SIP Analysis

* Monthly inflow trends
* Seasonal patterns

#### Investor Analytics

* Age distribution
* Gender analysis
* Geographic analysis

#### Portfolio Analytics

* Sector allocation
* Concentration analysis

### Outputs

* 15+ visualizations
* Key EDA insights document

---

## Day 4 – Fund Performance Analytics

### Metrics Implemented

* Daily Returns
* CAGR (1Y, 3Y, 5Y)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Tracking Error
* Maximum Drawdown

### Outputs

* fund_scorecard.csv
* alpha_beta.csv
* benchmark_comparison.png

---

## Day 5 – Power BI Dashboard Development

### Dashboard Pages

#### 1. Industry Overview

* Total Industry AUM
* SIP Growth Trends
* AMC Market Share
* Industry KPIs

#### 2. Fund Performance

* Risk vs Return Analysis
* Fund Ranking
* Benchmark Comparison
* NAV Trends

#### 3. Investor Analytics

* State-wise Investments
* Transaction Distribution
* Investor Demographics

#### 4. SIP & Market Trends

* Monthly SIP Trends
* Category Inflows
* Benchmark Tracking

#### 5. NAV Detail Page

* Drill-through analysis
* Fund-specific performance insights

### Outputs

* Power BI Dashboard
* Dashboard PDF
* Dashboard Screenshots

---

## Day 6 – Advanced Analytics & Risk Metrics

### Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio

### Investor Analytics

* Cohort Analysis
* SIP Continuity Analysis

### Recommendation Engine

* Rule-based Mutual Fund Recommendation System

### Portfolio Analysis

* Herfindahl-Hirschman Index (HHI)

### Outputs

* Advanced_Analytics.ipynb
* var_cvar_report.csv
* recommender.py
* rolling_sharpe_chart.png

---

# Key Business Insights

## Industry Insights

* SIP inflows demonstrated strong long-term growth.
* Equity funds contributed the highest inflow volumes.
* Large fund houses controlled the majority of industry AUM.

## Investor Insights

* Majority of investors belonged to the working-age segment.
* Urban regions contributed the largest SIP investments.
* Investor retention strongly influenced long-term growth.

## Fund Performance Insights

* High-performing funds consistently maintained superior Sharpe Ratios.
* Some schemes exhibited strong returns but elevated downside risk.
* Benchmark comparison highlighted outperforming schemes.

## Risk Insights

* VaR and CVaR identified schemes with higher downside exposure.
* Diversified portfolios showed lower concentration risk.
* Rolling Sharpe Ratio highlighted changing risk-adjusted performance over time.

---

# Dashboard Preview

The dashboard consists of:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends
5. NAV Detail Analysis

Screenshots are available in:

```text
dashboard/screenshots/
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/your-username/bluestock_mf_capstone.git

cd bluestock_mf_capstone
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Execute Complete Pipeline

```bash
python scripts/run_pipeline.py
```

This script will:

1. Ingest datasets
2. Clean data
3. Create database
4. Generate analytics
5. Export outputs

---

# Power BI Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

(Optional)

Publish to Power BI Service and add the public URL here.

---

# Project Deliverables

### Final Report

```text
reports/Final_Report.pdf
```

### Presentation

```text
reports/Bluestock_MF_Presentation.pptx
```

### Dashboard

```text
dashboard/bluestock_mf_dashboard.pbix
```

### Source Code

```text
scripts/
```

### Database

```text
data/db/
```

---

# Future Improvements

* Real-time NAV streaming
* Machine Learning-based fund recommendation system
* Portfolio optimization engine
* Predictive SIP growth forecasting
* Cloud deployment using Azure/AWS
* Automated dashboard refresh

---

# Self Review Checklist

* [x] All 8 project objectives completed
* [x] ETL pipeline functional
* [x] Database successfully created
* [x] SQL analytics completed
* [x] EDA completed
* [x] Performance analytics completed
* [x] Dashboard completed
* [x] Advanced risk metrics completed
* [x] Documentation completed
* [x] Final deliverables prepared


Rifa V P Zacharia

Bluestock Fintech Internship Capstone Project

2026



This project is developed for educational and internship purposes.

