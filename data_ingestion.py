
import pandas as pd
import os

# ── All 10 CSV datasets ────────────────────────────────────────────────
csv_files = [
    "data/raw/01_fund_master.csv",
    "data/raw/02_nav_history.csv",
    "data/raw/03_aum_by_fund_house.csv",
    "data/raw/04_monthly_sip_inflows.csv",
    "data/raw/05_category_inflows.csv",
    "data/raw/06_industry_folio_count.csv",
    "data/raw/07_scheme_performance.csv",
    "data/raw/08_investor_transactions.csv",
    "data/raw/09_portfolio_holdings.csv",
    "data/raw/10_benchmark_indices.csv",
]

anomaly_log = []

# ── Load, inspect, and check each CSV ─────────────────────────────────
for filepath in csv_files:
    name = os.path.basename(filepath)
    print(f"\n{'='*60}")
    print(f"FILE: {name}")
    print(f"{'='*60}")

    df = pd.read_csv(filepath)

    print(f"\n--- Shape ---")
    print(df.shape)

    print(f"\n--- dtypes ---")
    print(df.dtypes)

    print(f"\n--- Head ---")
    print(df.head())

    # ── Anomaly detection ──────────────────────────────────────────
    issues = []

    # Null check
    null_counts = df.isnull().sum()
    nulls = null_counts[null_counts > 0]
    if not nulls.empty:
        issues.append(f"  NULLS found: {nulls.to_dict()}")

    # Duplicate rows
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        issues.append(f"  DUPLICATE ROWS: {dup_count}")

    # Object columns that look numeric (formatting issues)
    for col in df.select_dtypes(include="object").columns:
        sample = df[col].dropna().head(10)
        try:
            pd.to_numeric(sample)
            issues.append(f"  DTYPE ISSUE: '{col}' looks numeric but stored as object")
        except:
            pass

    # Columns with all nulls
    all_null = df.columns[df.isnull().all()].tolist()
    if all_null:
        issues.append(f"  ALL-NULL COLUMNS: {all_null}")

    # Print anomaly summary for this file
    print(f"\n--- Anomaly Check ---")
    if issues:
        for issue in issues:
            print(issue)
        anomaly_log.append({"file": name, "issues": issues})
    else:
        print("  No anomalies detected.")

# ── Final Data Quality Summary ─────────────────────────────────────────
print(f"\n{'='*60}")
print("DATA QUALITY SUMMARY")
print(f"{'='*60}")
if anomaly_log:
    for entry in anomaly_log:
        print(f"\n{entry['file']}:")
        for issue in entry['issues']:
            print(issue)
else:
    print("All 10 files passed checks — no anomalies found.")
