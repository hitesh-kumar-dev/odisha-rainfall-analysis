import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/processed/odisha_rainfall_2020_2025.csv"
)

# Calculate district-wise statistics
district_stats = df.groupby("District")["Actual_Rainfall_mm"].agg(
    Average_Rainfall="mean",
    Total_Rainfall="sum",
    Maximum_Rainfall="max",
    Minimum_Rainfall="min"
).round(2)

# Sort by average rainfall
district_stats = district_stats.sort_values(
    by="Average_Rainfall",
    ascending=False
)

# Display all districts
print("\nDISTRICT-WISE RAINFALL ANALYSIS:")
print(district_stats)

# Top 5 districts
print("\nTOP 5 DISTRICTS BY AVERAGE RAINFALL:")
print(district_stats.head(5))

# Bottom 5 districts
print("\nBOTTOM 5 DISTRICTS BY AVERAGE RAINFALL:")
print(district_stats.tail(5))

# Save results
district_stats.to_csv(
    "data/processed/district_rainfall_analysis.csv"
)

print("\nDistrict analysis saved successfully!")