import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Before:", df.shape)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
      .str.upper()
      .str.strip()
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = [
    "Verified",
    "Pending"
]

invalid_rows = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print(
    "Invalid KYC rows:",
    len(invalid_rows)
)

# Remove invalid KYC
df = df[
    df["kyc_status"].isin(valid_kyc)
]

print("After:", df.shape)

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)