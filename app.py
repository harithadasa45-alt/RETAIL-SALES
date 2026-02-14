import streamlit as st
import pandas as pd

# Title
st.title("📊 Retail Sales Insights Dashboard")

# Load data
df = pd.read_csv("data/train.csv", parse_dates=["Order Date"], dayfirst=True)

# Extract month
df["Month"] = df["Order Date"].dt.month_name()

# Sidebar filter
month_selected = st.sidebar.selectbox("Select Month", df["Month"].unique())

# Filter data
filtered_df = df[df["Month"] == month_selected]

# Show total sales
st.subheader("Total Sales in Selected Month")
st.write(filtered_df["Sales"].sum())

# Top Selling Products
st.subheader("Top 5 Selling Products")
top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
st.bar_chart(top_products)

# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)
