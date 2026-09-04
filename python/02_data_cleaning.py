import pandas as pd
import os

print("Running Data Cleaning...")
os.makedirs('data/processed', exist_ok=True)
os.makedirs('reports', exist_ok=True)

df = pd.read_csv('data/raw/retail_sales_raw.csv')

# Generate Data Quality Report BEFORE cleaning
dq = pd.DataFrame({
    'Column': df.columns,
    'Null_Count': df.isnull().sum(),
    'Data_Type': df.dtypes
})
dq.to_csv('reports/data_quality_report.csv', index=False)
print("Saved data quality report to reports/data_quality_report.csv")

# Cleaning
# 1. Fill null Customer_IDs with 'UNKNOWN'
df['Customer_ID'] = df['Customer_ID'].fillna('UNKNOWN')

# 2. Fix negative quantities (take absolute value)
df['Quantity'] = df['Quantity'].abs()

# 3. Recalculate metrics just in case
df['Revenue'] = (df['Unit_Price'] * df['Quantity']) - df['Discount']
df['Cost'] = df['Unit_Cost'] * df['Quantity']
df['Profit'] = df['Revenue'] - df['Cost']

df.to_csv('data/processed/retail_sales_cleaned.csv', index=False)
print("Saved cleaned data to data/processed/retail_sales_cleaned.csv")
