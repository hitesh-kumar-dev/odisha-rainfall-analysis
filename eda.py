import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed/odisha_rainfall_2020_2025.csv"
)

# Basic information
print("\nDATASET INFORMATION:")
print(df.info())

# Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df["Actual_Rainfall_mm"].describe())

# Overall average rainfall
print("\nOVERALL AVERAGE RAINFALL:")
print(df["Actual_Rainfall_mm"].mean())

# Total rainfall across all observations
print("\nTOTAL OF DISTRICT-MONTH VALUES:")
print(df["Actual_Rainfall_mm"].sum())

# Average rainfall by year
print("\nYEAR-WISE AVERAGE RAINFALL:")
print(
    df.groupby("Year")["Actual_Rainfall_mm"]
    .mean()
    .round(2)
)

# Average rainfall by month
print("\nMONTH-WISE AVERAGE RAINFALL:")
print(
    df.groupby("Month")["Actual_Rainfall_mm"]
    .mean()
    .round(2)
)