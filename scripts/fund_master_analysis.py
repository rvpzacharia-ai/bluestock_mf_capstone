import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("UNIQUE FUND HOUSES")
print(df["fund_house"].nunique())
print(df["fund_house"].unique())

print("\n"+"="*60)
print("UNIQUE CATEGORIES")
print(df["category"].unique())

print("\n"+"="*60)
print("UNIQUE SUB CATEGORIES")
print(df["sub_category"].unique())

print("\n"+"="*60)
print("UNIQUE RISK CATEGORIES")
print(df["risk_category"].unique())