import pandas as pd
import matplotlib.pyplot as plt

# Load district-year comparison
df = pd.read_csv(
    "data/processed/district_year_comparison.csv",
    index_col=0
)

# Create figure
plt.figure(figsize=(12, 12))

# Create heatmap
plt.imshow(
    df.values,
    aspect="auto",
    interpolation="nearest"
)

# Add colour bar
plt.colorbar(label="Average Rainfall (mm)")

# Add axis labels
plt.xticks(
    range(len(df.columns)),
    df.columns
)

plt.yticks(
    range(len(df.index)),
    df.index
)

plt.title("District-wise Yearly Rainfall Heatmap (2020–2025)")
plt.xlabel("Year")
plt.ylabel("District")

plt.tight_layout()

# Save heatmap
plt.savefig(
    "data/processed/rainfall_heatmap.png",
    dpi=300
)

plt.show()

print("Rainfall heatmap saved successfully!")