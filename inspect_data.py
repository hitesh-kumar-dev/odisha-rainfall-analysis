import pandas as pd
import os

years = range(2020, 2026)

for year in years:

    file_path = f"data/raw/rainfall_{year}.xls"
    sheet_name = f"Abstract_{year}"

    print(f"\n{'='*40}")
    print(f"YEAR: {year}")
    print(f"{'='*40}")

    if not os.path.exists(file_path):
        print(f"FILE NOT FOUND: {file_path}")
        continue

    try:
        df = pd.read_excel(
            file_path,
            sheet_name=sheet_name,
            header=2,
            engine="xlrd"
        )

        # Remove summary rows
        df = df.dropna(subset=["District"])

        # Clean district names
        df["District"] = df["District"].str.strip()

        print("Dataset shape:", df.shape)
        print("District count:", df["District"].nunique())
        print("Columns:", df.columns.tolist())
        print("Missing values:", df.isnull().sum().sum())

    except Exception as e:
        print("ERROR:", e)