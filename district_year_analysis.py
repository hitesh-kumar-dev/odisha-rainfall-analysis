import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/processed/odisha_rainfall_2020_2025.csv"
)

# Calculate average rainfall for each district and year
district_year = df.pivot_table(
    index="District",
    columns="Year",
    values="Actual_Rainfall_mm",
    aggfunc="mean"
).round(2)

# Display results
print("\nDISTRICT-WISE YEARLY AVERAGE RAINFALL:")
print(district_year)

# Save results
district_year.to_csv(
    "data/processed/district_year_comparison.csv"
)

print("\nDistrict-year analysis saved successfully!")