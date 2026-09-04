import pandas as pd

print("Running EDA...")
df = pd.read_csv('data/processed/retail_sales_cleaned.csv')

print("\nSummary Statistics:")
print(df.describe())

print("\nTop 5 Categories by Revenue:")
print(df.groupby('Category')['Revenue'].sum().sort_values(ascending=False).head(5))
