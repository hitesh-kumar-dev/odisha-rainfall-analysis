import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "data/processed/odisha_rainfall_2020_2025.csv"
)

# Month order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Year-wise average rainfall
yearly_rainfall = (
    df.groupby("Year")["Actual_Rainfall_mm"]
    .mean()
)

plt.figure(figsize=(10, 5))
yearly_rainfall.plot(kind="bar")

plt.title("Average Rainfall in Odisha (2020–2025)")
plt.xlabel("Year")
plt.ylabel("Average Rainfall (mm)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("data/processed/yearly_rainfall.png")
plt.show()


# Month-wise average rainfall
monthly_rainfall = (
    df.groupby("Month")["Actual_Rainfall_mm"]
    .mean()
    .reindex(month_order)
)

plt.figure(figsize=(12, 5))
monthly_rainfall.plot(kind="bar")

plt.title("Average Monthly Rainfall in Odisha (2020–2025)")
plt.xlabel("Month")
plt.ylabel("Average Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/processed/monthly_rainfall.png")
plt.show()


# Overall rainfall distribution
plt.figure(figsize=(10, 5))
df["Actual_Rainfall_mm"].plot(kind="hist", bins=30)

plt.title("Distribution of Rainfall in Odisha")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("data/processed/rainfall_distribution.png")
plt.show()