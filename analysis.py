import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("city_cost_data.csv")

# Set baseline city (Milwaukee)
baseline_city = "Milwaukee"
baseline_index = df.loc[df["city"] == baseline_city, "cost_of_living_index"].values[0]

# Calculate salary equivalent
df["salary_equivalent"] = (df["cost_of_living_index"] / baseline_index) * 70000

# Sort for plotting
df = df.sort_values("salary_equivalent")

# Plot
plt.figure()
plt.barh(df["city"], df["salary_equivalent"])
plt.xlabel("Equivalent Salary ($)")
plt.title("Salary Needed to Match Milwaukee Living Standard ($70k)")
plt.tight_layout()
plt.savefig("figures/salary_equivalent.png")
plt.close()
