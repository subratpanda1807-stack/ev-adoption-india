import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Dataset.xlsx")

# Total EV sales by year
yearly_sales = df.groupby("Year")["EV_Sales_Quantity"].sum()
print("EV Sales by Year:")
print(yearly_sales)

# Top 10 states by total EV sales
state_sales = df.groupby("State")["EV_Sales_Quantity"].sum(
).sort_values(ascending=False).head(10)
print("\nTop 10 States by EV Sales:")
print(state_sales)


# Chart 1 - EV Sales Growth by Year
plt.figure(figsize=(10, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o', color='green')
plt.title("EV Sales Growth in India (2014-2023)")
plt.xlabel("Year")
plt.ylabel("Total EV Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("yearly_sales.png")
plt.show()
print("Chart 1 saved")


# Chart 2 - Top 10 States Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(state_sales.index, state_sales.values, color='steelblue')
plt.title("Top 10 States by EV Sales")
plt.xlabel("State")
plt.ylabel("Total EV Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("state_sales.png")
plt.show()
print("Chart 2 saved")


# Chart 3 - EV Sales by Vehicle Category
category_sales = df.groupby("Vehicle_Category")[
    "EV_Sales_Quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(category_sales.index, category_sales.values, color='coral')
plt.title("EV Sales by Vehicle Category")
plt.xlabel("Vehicle Category")
plt.ylabel("Total EV Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()
print("Chart 3 saved")


# Export summary to Excel
summary = pd.DataFrame({
    "Year": yearly_sales.index,
    "Total_EV_Sales": yearly_sales.values
})

summary.to_excel("EV_Summary.xlsx", index=False)
print("Summary exported to EV_Summary.xlsx")
