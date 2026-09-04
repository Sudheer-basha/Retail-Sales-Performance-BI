import pandas as pd

print("Running Store & Product Analysis...")
df = pd.read_csv('data/processed/retail_sales_cleaned.csv')

top_stores = df.groupby('Store_Name')['Revenue'].sum().sort_values(ascending=False)
print("Top Stores by Revenue:")
print(top_stores.head())
