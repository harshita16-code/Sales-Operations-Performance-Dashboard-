import pandas as pd
import matplotlib.pyplot as plt

# =============================
# Load Sample Data
# =============================
sales_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Sales": [50000, 30000, 40000, 45000]
})

operations_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Total_Ops": [200, 150, 180, 220],
    "Successful_Ops": [180, 120, 150, 200]
})

# =============================
# 1. Sales by Region Bar Chart
# =============================
plt.figure(figsize=(6,4))
plt.bar(sales_data["Region"], sales_data["Sales"])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.savefig("dashboards/sales_by_region.png")
plt.close()

# =============================
# 2. Operational Efficiency
# =============================
operations_data["Efficiency %"] = (
    operations_data["Successful_Ops"] / operations_data["Total_Ops"] * 100
)

plt.figure(figsize=(6,4))
plt.bar(operations_data["Region"], operations_data["Efficiency %"], color="green")
plt.title("Operational Efficiency by Region")
plt.xlabel("Region")
plt.ylabel("Efficiency %")
plt.savefig("dashboards/efficiency_by_region.png")
plt.close()

# =============================
# 3. Combined Sales vs Efficiency
# =============================
combined = pd.merge(sales_data, operations_data, on="Region")

plt.figure(figsize=(6,4))
plt.scatter(combined["Sales"], combined["Efficiency %"], color="purple")
for i, txt in enumerate(combined["Region"]):
    plt.annotate(txt, (combined["Sales"][i], combined["Efficiency %"][i]))
plt.title("Sales vs Efficiency")
plt.xlabel("Sales")
plt.ylabel("Efficiency %")
plt.savefig("dashboards/sales_vs_efficiency.png")
plt.close()
