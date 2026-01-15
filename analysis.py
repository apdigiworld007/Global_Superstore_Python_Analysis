"""
Global Superstore USA – Python Analysis
Time Period: 2014–2017
Author: Amir Payara
"""

import pandas as pd

file_path = r"C:\Users\amirp\OneDrive\Documents\Global Superstore s\Global_Superstore_Python_Analysis\data\Global_Superstore_Orders_USA.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("✅ Data loaded successfully")
print("Rows & Columns:", df.shape)
print("\nColumns:")
print(df.columns)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df_2014_2017 = df[
    (df['Order Date'].dt.year >= 2014) &
    (df['Order Date'].dt.year <= 2017)
]
# Total Sales, Total Profit, Total Orders (2014–2017)
core_kpis = (
    df_2014_2017
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Total_Orders=('Order ID', 'nunique')
    )
)

print(core_kpis)

# Monthly Sales & Profit for year 2014 to 2017
monthly_trend = (
    df_2014_2017
    .groupby([
        df_2014_2017['Order Date'].dt.year.rename('Year'),
        df_2014_2017['Order Date'].dt.month.rename('Month')
    ])
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .sort_values(['Year', 'Month'])
)

print(monthly_trend)
# Product Categories — Which categories generate the most sales?(2014-2017)
## Aggregate Sales by Category

category_sales = (
    df_2014_2017
    .groupby('Category')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .sort_values('Total_Sales', ascending=False)
)

print(category_sales)
# Which states contribute the highest revenue?(2014-2017 USA)
## Revenue by State (Top 10)
state_sales = (
    df_2014_2017
    .groupby('State')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .sort_values('Total_Sales', ascending=False)
)

print(state_sales.head(10))
# Which products are loss-making? (Negative Profit)
## Identify Loss-Making Products
loss_making_products = (
    df_2014_2017
    .groupby('Product Name')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .query('Total_Profit < 0')
    .sort_values('Total_Profit')
)

print(loss_making_products.head(10))

# Top 5 Customers by Sales
top_5_customers = (
    df_2014_2017
    .groupby('Customer Name')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .sort_values('Total_Sales', ascending=False)
    .head(5)
)

print(top_5_customers)

