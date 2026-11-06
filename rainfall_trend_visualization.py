import pandas as pd
import matplotlib.pyplot as plt
import os

# Load rainfall trend data
df = pd.read_csv(
    "data/processed/rainfall_trends.csv"
)

# Sort districts by percentage change
df = df.sort_values(
    by="Percentage_Change",
    ascending=True
)

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Create horizontal bar chart
plt.figure(figsize=(12, 10))

plt.barh(
    df["District"],
    df["Percentage_Change"]
)

# Add zero reference line
plt.axvline(x=0, linestyle="--")

# Chart labels
plt.title("District-wise Rainfall Change in Odisha (2020–2025)")
plt.xlabel("Rainfall Change (%)")
plt.ylabel("District")

plt.tight_layout()

# Save visualization
plt.savefig(
    "images/rainfall_trends.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Rainfall trend visualization saved successfully!")