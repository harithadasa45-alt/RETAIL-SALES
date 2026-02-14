# 🛒 Retail Sales Insights Dashboard

## 📌 Project Overview

The **Retail Sales Insights Dashboard** is a data analysis project designed to extract meaningful business insights from a retail sales dataset.  

The goal of this project is to analyze sales performance, identify top-performing products and regions, understand monthly revenue trends, and examine the relationship between sales and profit.

This project demonstrates foundational skills required for a Data Analyst role, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Aggregation
- SQL Query Writing
- Data Visualization
- Dashboard Creation

---

## 📂 Dataset Information

- Dataset Name: Superstore Sales Dataset
- Source: Kaggle
- File Format: CSV

### Key Columns Used:

- Order Date
- Product Name
- Category
- Region
- Sales
- Profit
- Quantity

---

## 🛠️ Tools & Technologies Used

### 🐍 Python
- Pandas – Data manipulation and aggregation
- Matplotlib – Data visualization
- Jupyter Notebook – Analysis environment

### 🗄️ SQL
- GROUP BY
- ORDER BY
- Aggregate functions (SUM)
- Date functions

### 📊 Power BI
- Interactive dashboard creation
- Visual representation of KPIs

### 🔧 Version Control
- Git
- GitHub

---

## 🔍 Business Questions Answered

1. Which product generates the highest total sales?
2. What is the monthly revenue trend?
3. Which region performs best in terms of total sales?
4. What is the relationship between sales and profit?

---

## 📊 Exploratory Data Analysis (EDA)

### 1️⃣ Top Selling Products

Grouped the dataset by Product Name and calculated total sales to identify high-performing products.

Key Insight:
- Identified top 5 products contributing the highest revenue.

---

### 2️⃣ Monthly Revenue Trend

Converted "Order Date" into datetime format and extracted monthly data to analyze revenue patterns.

Key Insight:
- Observed sales growth patterns across different months.
- Identified peak revenue months.

---

### 3️⃣ Regional Sales Performance

Aggregated sales by Region to determine which region generates the highest revenue.

Key Insight:
- Determined the most profitable region.
- Compared regional sales performance.

---

### 4️⃣ Profit vs Sales Analysis

Created a scatter plot to visualize the relationship between Sales and Profit.

Key Insight:
- Observed correlation between higher sales and profitability.
- Identified instances where high sales did not always result in high profit.

---

## 🧾 SQL Queries Included

The project includes SQL queries to:

- Retrieve top-selling products
- Calculate monthly sales
- Analyze regional sales performance
- Perform aggregations using GROUP BY and SUM

SQL file location:
```
/sql/queries.sql
```

---

## 📈 Dashboard

An interactive dashboard was created using Power BI to visually present:

- Total Sales KPI
- Monthly Sales Trend (Line Chart)
- Sales by Region (Bar Chart)
- Profit Analysis

Dashboard screenshot available in:
```
/dashboard/
```

---

## 📁 Project Structure

```
Retail-Sales-Insights-Dashboard/
│
├── data/
│   └── superstore.csv
│
├── notebook/
│   └── sales_analysis.ipynb
│
├── sql/
│   └── queries.sql
│
├── dashboard/
│   └── dashboard_screenshot.png
│
└── README.md
```

---

## 🎯 Key Skills Demonstrated

- Data Cleaning & Preparation
- Exploratory Data Analysis
- Business Insight Extraction
- SQL Query Writing
- Data Visualization
- Dashboard Reporting
- Git & GitHub Version Control

---

## 🚀 How to Run This Project

1. Clone the repository
   ```
   git clone <repository-link>
   ```

2. Navigate to the project folder
   ```
   cd Retail-Sales-Insights-Dashboard
   ```

3. Install required libraries
   ```
   pip install pandas matplotlib seaborn
   ```

4. Open Jupyter Notebook
   ```
   jupyter notebook
   ```

5. Run `sales_analysis.ipynb`

---

## 📌 Conclusion

This project provides practical experience in analyzing retail sales data and transforming raw data into meaningful business insights.  

It demonstrates core data analytics skills and reflects the ability to work with real-world datasets using Python, SQL, and visualization tools.

---

## 👩‍💻 Author

Haritha Dasa  
MCA Final Year Student  
Aspiring Data Analyst
