import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Before:", df.shape)

# date → datetime
df["date"] = pd.to_datetime(df["date"])

# sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# remove duplicates
df = df.drop_duplicates()

# NAV > 0
df = df[df["nav"] > 0]

# forward fill missing NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

print("After:", df.shape)

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)