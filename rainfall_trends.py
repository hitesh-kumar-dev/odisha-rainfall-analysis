import pandas as pd

# Load district-year comparison
df = pd.read_csv(
    "data/processed/district_year_comparison.csv",
    index_col=0
)

# Calculate rainfall difference
df["Rainfall_Change"] = df["2025"] - df["2020"]

# Calculate percentage change
df["Percentage_Change"] = (
    (df["Rainfall_Change"] / df["2020"]) * 100
).round(2)

# Classify rainfall trends
df["Trend"] = df["Rainfall_Change"].apply(
    lambda x: "Increasing" if x > 0
    else "Decreasing" if x < 0
    else "No Change"
)

# Display all district trends
print("\nDISTRICT-WISE RAINFALL TRENDS:")
print(
    df[["2020", "2025", "Rainfall_Change",
        "Percentage_Change", "Trend"]]
)

# Districts with increasing rainfall
increasing = df[df["Trend"] == "Increasing"]

print("\nDISTRICTS WITH INCREASING RAINFALL:")
print(increasing[["Rainfall_Change", "Percentage_Change"]])

# Districts with decreasing rainfall
decreasing = df[df["Trend"] == "Decreasing"]

print("\nDISTRICTS WITH DECREASING RAINFALL:")
print(decreasing[["Rainfall_Change", "Percentage_Change"]])

# Summary
print("\nTREND SUMMARY:")
print("Increasing districts:", len(increasing))
print("Decreasing districts:", len(decreasing))

# Save results
df.to_csv("data/processed/rainfall_trends.csv")

print("\nRainfall trend analysis saved successfully!")