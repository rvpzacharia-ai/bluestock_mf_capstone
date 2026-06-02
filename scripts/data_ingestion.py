from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

csv_files = raw_path.glob("*.csv")

for file in csv_files:

    print("="*60)
    print("File:", file.name)

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())
    