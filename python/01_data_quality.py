import pandas as pd
import os

print("Running Data Quality Checks...")
df = pd.read_csv('data/raw/retail_sales_raw.csv')

print(f"Dataset shape: {df.shape}")
print("\nNull Values:")
print(df.isnull().sum())

print("\nNegative Quantities:")
print((df['Quantity'] < 0).sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("Data Quality Check Complete.")
