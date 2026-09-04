import pandas as pd

print("Running Sales Analysis...")
df = pd.read_csv('data/processed/retail_sales_cleaned.csv')
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

monthly_sales = df.groupby(df['Transaction_Date'].dt.to_period('M'))['Revenue'].sum()
print("Monthly Sales:")
print(monthly_sales)
