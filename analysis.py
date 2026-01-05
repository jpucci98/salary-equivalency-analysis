import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("city_cost_data.csv")

# Baseline
baseline_city = "Milwaukee"
baseline_salary = 70000
baseline_index = df.loc[df["city"] == baseline_city, "cost_of_living_index"].values[0]

# Salary equivalent calculation
df["salary_equivalent"] = (df["cost_of_living_index"] / baseline_index) * baseline_salary

# ----------------------------
# Chart 1: Salary Equivalent
# ----------------------------
df_sorted = df.sort_values("salary_equivalent")

plt.figure()
plt.barh(df_sorted["city"], df_sorted["salary_equivalent"])
plt.xlabel("Equivalent Salary ($)")
plt.title("Salary Needed to Match Milwaukee Living Standard ($70k)")
plt.tight_layout()
plt.savefig("figures/salary_equivalent.png")
plt.close()

# ----------------------------
# Chart 2: Nominal vs Real Comparison
# ----------------------------
df["nominal_salary"] = baseline_salary

plt.figure()
plt.plot(df["city"], df["nominal_salary"], label="Nominal Salary")
plt.plot(df["city"], df["salary_equivalent"], label="Cost-Adjusted Salary")
plt.xticks(rotation=45)
plt.ylabel("Salary ($)")
plt.title("Nominal vs Cost-Adjusted Salary by City")
plt.legend()
plt.tight_layout()
plt.savefig("figures/nominal_vs_real.png")
plt.close()
