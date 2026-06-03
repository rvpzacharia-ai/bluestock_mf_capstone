import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# expense ratio validation
anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense anomalies:",
    len(anomalies)
)

anomalies.to_csv(
    "reports/expense_ratio_anomalies.csv",
    index=False
)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)