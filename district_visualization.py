import pandas as pd
import matplotlib.pyplot as plt

# Load district analysis
df = pd.read_csv(
    "data/processed/district_rainfall_analysis.csv"
)

# Sort districts by average rainfall
df = df.sort_values(
    by="Average_Rainfall",
    ascending=True
)

# Create horizontal bar chart
plt.figure(figsize=(12, 10))

plt.barh(
    df["District"],
    df["Average_Rainfall"]
)

plt.title("District-wise Average Rainfall in Odisha (2020–2025)")
plt.xlabel("Average Rainfall (mm)")
plt.ylabel("District")

plt.tight_layout()

# Save figure
plt.savefig(
    "data/processed/district_rainfall.png",
    dpi=300
)

plt.show()

print("District-wise visualization saved successfully!")