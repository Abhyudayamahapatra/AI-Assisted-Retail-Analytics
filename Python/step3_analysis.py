import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/orders_cleaned.csv")

print("Dataset Shape:", df.shape)

# 1. Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# 2. Total Profit
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# 3. Sales by Category
sales_by_category = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(sales_by_category)

# 4. Profit by Region
profit_by_region = df.groupby('Region')['Profit'].sum()
print("\nProfit by Region:")
print(profit_by_region)

# 5. Monthly Sales Trend
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

# 6. Top 10 Products
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products:")
print(top_products)