import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("data/train.csv")

print("Dataset Loaded Successfully!\n")

# Show first 5 rows
print("First 5 Rows:\n")
print(df.head())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Top 5 Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print("\nTop 5 Selling Products:\n")
print(top_products.head())

# Sales by Region
#region_sales = df.groupby("Region")["Sales"].sum()

#print("\nSales by Region:\n")
#print(region_sales)
#plt.figure()
#region_sales.plot(kind="bar")
#plt.title("Sales by Region")
#plt.xlabel("Region")
#plt.ylabel("Total Sales")
#plt.tight_layout()
#plt.show()
#Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("monthly_sales_trend.png")
plt.show()
# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
