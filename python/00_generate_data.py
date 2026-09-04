import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Ensure directories exist
os.makedirs('data/raw', exist_ok=True)

# Configurations
num_records = 100000

# Data generation
print(f"Generating {num_records} records of retail sales data...")

# Dates
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = (end_date - start_date).days
dates = [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(num_records)]

# Stores
stores = [
    {'Store_ID': 'ST001', 'Store_Name': 'Downtown Superstore', 'Region': 'East', 'State': 'New York', 'City': 'New York'},
    {'Store_ID': 'ST002', 'Store_Name': 'Midtown Mall', 'Region': 'East', 'State': 'New York', 'City': 'New York'},
    {'Store_ID': 'ST003', 'Store_Name': 'Westside Plaza', 'Region': 'West', 'State': 'California', 'City': 'Los Angeles'},
    {'Store_ID': 'ST004', 'Store_Name': 'Valley Center', 'Region': 'West', 'State': 'California', 'City': 'San Jose'},
    {'Store_ID': 'ST005', 'Store_Name': 'Northern Hub', 'Region': 'Midwest', 'State': 'Illinois', 'City': 'Chicago'},
    {'Store_ID': 'ST006', 'Store_Name': 'Southern Outlet', 'Region': 'South', 'State': 'Texas', 'City': 'Houston'},
    {'Store_ID': 'ST007', 'Store_Name': 'Gulf Coast Shop', 'Region': 'South', 'State': 'Texas', 'City': 'Austin'},
    {'Store_ID': 'ST008', 'Store_Name': 'Sunshine Mall', 'Region': 'South', 'State': 'Florida', 'City': 'Miami'},
    {'Store_ID': 'ST009', 'Store_Name': 'Mountain View', 'Region': 'West', 'State': 'Colorado', 'City': 'Denver'},
    {'Store_ID': 'ST010', 'Store_Name': 'Capitol Store', 'Region': 'East', 'State': 'Washington', 'City': 'Seattle'},
]

store_selections = [random.choice(stores) for _ in range(num_records)]

# Customers
customer_types = ['Regular', 'Premium', 'New', 'Guest']
cust_type_probs = [0.4, 0.2, 0.3, 0.1]
customer_types_col = np.random.choice(customer_types, num_records, p=cust_type_probs)
customer_ids = [f"C{str(random.randint(1000, 9999))}" if ct != 'Guest' else "GUEST" for ct in customer_types_col]

# Products
categories = {
    'Electronics': [
        ('Laptops', 'PRD01', 'Pro Laptop 15', 800, 1200),
        ('Laptops', 'PRD02', 'Basic Laptop 13', 300, 500),
        ('Smartphones', 'PRD03', 'Flagship Phone', 500, 999),
        ('Smartphones', 'PRD04', 'Budget Phone', 150, 299),
        ('Accessories', 'PRD05', 'Wireless Earbuds', 30, 99),
        ('Accessories', 'PRD06', 'Smart Watch', 100, 250),
    ],
    'Clothing': [
        ('Mens', 'PRD07', 'Cotton T-Shirt', 5, 20),
        ('Mens', 'PRD08', 'Jeans', 20, 60),
        ('Womens', 'PRD09', 'Summer Dress', 15, 45),
        ('Womens', 'PRD10', 'Designer Blouse', 30, 80),
        ('Kids', 'PRD11', 'Kids Sneakers', 10, 35),
    ],
    'Home & Garden': [
        ('Furniture', 'PRD12', 'Office Chair', 50, 150),
        ('Furniture', 'PRD13', 'Bookshelf', 40, 120),
        ('Decor', 'PRD14', 'Table Lamp', 15, 40),
        ('Decor', 'PRD15', 'Wall Art', 25, 75),
        ('Garden', 'PRD16', 'Planter Set', 20, 50),
    ],
    'Groceries': [
        ('Snacks', 'PRD17', 'Organic Chips', 2, 5),
        ('Snacks', 'PRD18', 'Mixed Nuts', 3, 8),
        ('Beverages', 'PRD19', 'Sparkling Water', 1, 3),
        ('Beverages', 'PRD20', 'Craft Coffee', 5, 15),
    ]
}

all_products = []
for cat, prods in categories.items():
    for p in prods:
        all_products.append({'Category': cat, 'Sub_Category': p[0], 'Product_ID': p[1], 'Product_Name': p[2], 'Unit_Cost': p[3], 'Unit_Price': p[4]})

product_selections = [random.choice(all_products) for _ in range(num_records)]

# Create basic dataframe
df = pd.DataFrame({
    'Transaction_ID': [f"TRX{str(i).zfill(6)}" for i in range(1, num_records + 1)],
    'Transaction_Date': dates,
    'Store_ID': [s['Store_ID'] for s in store_selections],
    'Store_Name': [s['Store_Name'] for s in store_selections],
    'Region': [s['Region'] for s in store_selections],
    'State': [s['State'] for s in store_selections],
    'City': [s['City'] for s in store_selections],
    'Customer_ID': customer_ids,
    'Customer_Type': customer_types_col,
    'Product_ID': [p['Product_ID'] for p in product_selections],
    'Product_Name': [p['Product_Name'] for p in product_selections],
    'Category': [p['Category'] for p in product_selections],
    'Sub_Category': [p['Sub_Category'] for p in product_selections],
    'Unit_Cost': [p['Unit_Cost'] for p in product_selections],
    'Unit_Price': [p['Unit_Price'] for p in product_selections],
})

# Quantities
df['Quantity'] = np.random.choice([1, 2, 3, 4, 5, 10], num_records, p=[0.6, 0.2, 0.1, 0.05, 0.03, 0.02])

# Introduce some noise/nulls for data cleaning practice
# 1% nulls in Customer_ID
mask = np.random.choice([True, False], num_records, p=[0.01, 0.99])
df.loc[mask, 'Customer_ID'] = np.nan

# 0.5% negative quantities (errors)
mask = np.random.choice([True, False], num_records, p=[0.005, 0.995])
df.loc[mask, 'Quantity'] = -1 * df.loc[mask, 'Quantity']

# Promotions and discounts
promotions = ['None', 'Holiday Sale', 'Clearance', 'BOGO', 'Weekend Special']
df['Promotion'] = np.random.choice(promotions, num_records, p=[0.7, 0.1, 0.05, 0.05, 0.1])

# Calculate Discount based on promotion
df['Discount'] = 0.0
df.loc[df['Promotion'] == 'Holiday Sale', 'Discount'] = df.loc[df['Promotion'] == 'Holiday Sale', 'Unit_Price'] * 0.15 * df['Quantity']
df.loc[df['Promotion'] == 'Clearance', 'Discount'] = df.loc[df['Promotion'] == 'Clearance', 'Unit_Price'] * 0.30 * df['Quantity']
df.loc[df['Promotion'] == 'BOGO', 'Discount'] = df.loc[df['Promotion'] == 'BOGO', 'Unit_Price'] * 0.50 * df['Quantity']
df.loc[df['Promotion'] == 'Weekend Special', 'Discount'] = df.loc[df['Promotion'] == 'Weekend Special', 'Unit_Price'] * 0.10 * df['Quantity']
df.loc[df['Customer_Type'] == 'Premium', 'Discount'] += df.loc[df['Customer_Type'] == 'Premium', 'Unit_Price'] * 0.05 * df['Quantity']

# Round discount
df['Discount'] = df['Discount'].round(2)

# Calculate financial metrics
df['Revenue'] = (df['Unit_Price'] * df['Quantity']) - df['Discount']
df['Cost'] = df['Unit_Cost'] * df['Quantity']
df['Profit'] = df['Revenue'] - df['Cost']

# Payment modes
payment_modes = ['Credit Card', 'Debit Card', 'Cash', 'Mobile App', 'Gift Card']
df['Payment_Mode'] = np.random.choice(payment_modes, num_records, p=[0.45, 0.25, 0.15, 0.1, 0.05])

# Return flag (more likely for certain categories like Clothing)
df['Return_Flag'] = 'N'
clothing_mask = df['Category'] == 'Clothing'
df.loc[clothing_mask, 'Return_Flag'] = np.random.choice(['Y', 'N'], clothing_mask.sum(), p=[0.15, 0.85])
df.loc[~clothing_mask, 'Return_Flag'] = np.random.choice(['Y', 'N'], (~clothing_mask).sum(), p=[0.05, 0.95])

# If returned, revenue is 0 but cost might still be there, let's just mark it Y/N for simplicity
# Sort by date
df = df.sort_values('Transaction_Date').reset_index(drop=True)
df['Transaction_Date'] = df['Transaction_Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

df.to_csv('data/raw/retail_sales_raw.csv', index=False)
print(f"Data generation complete. File saved to 'data/raw/retail_sales_raw.csv'. Total records: {len(df)}")
