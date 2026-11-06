import pandas as pd
import os

# Years to process
years = range(2020, 2026)

# Monthly columns
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

all_data = []

# Process each year's Excel file
for year in years:

    file_path = f"data/raw/rainfall_{year}.xls"
    sheet_name = f"Abstract_{year}"

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

    # Keep only required columns
    df = df[["District"] + months]

    # Convert wide format into long format
    df_long = df.melt(
        id_vars=["District"],
        value_vars=months,
        var_name="Month",
        value_name="Actual_Rainfall_mm"
    )

    # Add year
    df_long["Year"] = year

    all_data.append(df_long)

# Combine all years
final_df = pd.concat(all_data, ignore_index=True)

# Arrange columns
final_df = final_df[
    ["District", "Year", "Month", "Actual_Rainfall_mm"]
]

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Save combined dataset
output_path = "data/processed/odisha_rainfall_2020_2025.csv"

final_df.to_csv(output_path, index=False)

# Display results
print("\nCOMBINED DATASET:")
print(final_df.head(10))

print("\nDATASET SHAPE:")
print(final_df.shape)

print("\nUNIQUE DISTRICTS:")
print(final_df["District"].nunique())

print("\nYEARS:")
print(sorted(final_df["Year"].unique()))

print("\nMISSING VALUES:")
print(final_df.isnull().sum())

print("\nFILE SAVED SUCCESSFULLY:")
print(output_path)  