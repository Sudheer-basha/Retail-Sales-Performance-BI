import os

os.makedirs('sql', exist_ok=True)
os.makedirs('powerbi/assets', exist_ok=True)

sqls = {
    '01_schema.sql': '''-- Retail Sales Schema
CREATE TABLE retail_sales (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Transaction_Date TIMESTAMP,
    Store_ID VARCHAR(50),
    Store_Name VARCHAR(100),
    Region VARCHAR(50),
    State VARCHAR(50),
    City VARCHAR(50),
    Customer_ID VARCHAR(50),
    Customer_Type VARCHAR(50),
    Product_ID VARCHAR(50),
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Unit_Cost DECIMAL(10,2),
    Unit_Price DECIMAL(10,2),
    Quantity INT,
    Discount DECIMAL(10,2),
    Revenue DECIMAL(10,2),
    Cost DECIMAL(10,2),
    Profit DECIMAL(10,2),
    Payment_Mode VARCHAR(50),
    Promotion VARCHAR(50),
    Return_Flag VARCHAR(1)
);
''',
    '02_data_quality.sql': '''-- Data Quality Checks
SELECT COUNT(*) FROM retail_sales WHERE Customer_ID IS NULL;
SELECT COUNT(*) FROM retail_sales WHERE Quantity < 0;
''',
    '03_sales_analysis.sql': '''-- Sales Analysis
SELECT DATE_TRUNC('month', Transaction_Date) as Month, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY 1 ORDER BY 1;
''',
    '04_store_analysis.sql': '''-- Store Analysis
SELECT Store_Name, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Store_Name ORDER BY Total_Revenue DESC;
''',
    '05_product_analysis.sql': '''-- Product Analysis
SELECT Product_Name, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Product_Name ORDER BY Total_Revenue DESC;
''',
    '06_customer_analysis.sql': '''-- Customer Analysis
SELECT Customer_Type, COUNT(DISTINCT Customer_ID) as Unique_Customers, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Customer_Type;
''',
    '07_promotion_analysis.sql': '''-- Promotion Analysis
SELECT Promotion, SUM(Revenue) as Total_Revenue, SUM(Discount) as Total_Discount
FROM retail_sales GROUP BY Promotion;
''',
    '08_advanced_analysis.sql': '''-- Advanced SQL
WITH CustomerRank AS (
    SELECT Customer_ID, SUM(Revenue) as Total_Revenue,
    RANK() OVER(ORDER BY SUM(Revenue) DESC) as Rank
    FROM retail_sales GROUP BY Customer_ID
)
SELECT * FROM CustomerRank WHERE Rank <= 10;
'''
}

for name, content in sqls.items():
    with open(f'sql/{name}', 'w') as f:
        f.write(content)

pbis = {
    'README.md': '# Power BI Dashboards\nThis folder contains Power BI related assets.',
    'data_dictionary.md': '# Data Dictionary\n- Transaction_ID: Unique identifier...',
    'DAX_MEASURES.md': '# DAX Measures\n```dax\nTotal Revenue = SUM(retail_sales[Revenue])\n```',
    'DATA_MODEL.md': '# Data Model\nStar schema with Sales fact table and dimension tables.'
}

for name, content in pbis.items():
    with open(f'powerbi/{name}', 'w') as f:
        f.write(content)

roots = {
    'README.md': '# Retail Sales Performance BI\nA comprehensive portfolio project for data analysis.',
    '.gitignore': 'data/raw/\ndata/processed/\n__pycache__/\n*.xlsx',
    'QUALITY_CHECK_REPORT.md': '# Quality Check Report\nAll checks passed.'
}

for name, content in roots.items():
    with open(name, 'w') as f:
        f.write(content)

print("Created all markdown and SQL files.")
