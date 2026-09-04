# Retail Sales Performance & Business Intelligence

A comprehensive data analytics portfolio project analyzing retail sales across products, stores, regions, customers, and time to identify revenue drivers, profitability issues, seasonal trends, and underperforming business areas.

## Business Problem
The retail chain operates across multiple regions and stores, but leadership lacks clear visibility into which specific stores, product categories, and promotional campaigns are actually driving net profitability versus just top-line revenue.

## Objective
To build an end-to-end retail BI pipeline that processes 100,000+ transactional records to uncover actionable insights regarding store performance, product profitability, and customer purchasing behaviors using Python, SQL, Excel, and Power BI.

## Dataset
- **Volume:** 100,000+ transaction records.
- **Scope:** Includes transaction details, store locations, product hierarchies, financials (Revenue, Cost, Profit), and promotional/return flags.

## Data Dictionary
| Column | Description |
|---|---|
| `Transaction_ID` | Unique identifier for the sale |
| `Store_ID` / `Store_Name` | Location of the sale |
| `Product_Name` | Name of the product sold |
| `Category` | High-level product category (e.g., Electronics, Clothing) |
| `Revenue` | Total sales revenue |
| `Profit` | Net profit (Revenue - Cost) |
| `Promotion` | Was a promotion applied? (Yes/No) |
| `Return_Flag` | Was the item returned? (1/0) |

## Tools & Technologies
- **Python:** `pandas`, `numpy` (Data Processing, EDA, Missing Value Imputation)
- **SQL:** Complex Joins, Aggregations, CTEs, Window functions for store/product ranking
- **Excel:** Automated Pivot Tables, KPI Summaries, formatting via `xlsxwriter`
- **Power BI:** Data Modeling, DAX Measures for executive dashboarding

## Project Architecture
1. **Data Generation & Quality Check:** Synthetic realistic 100k+ row retail dataset generated and validated.
2. **Data Cleaning (Python):** Handling missing values, standardizing text fields, and validating financial logic (Revenue = Cost + Profit).
3. **Database Analysis (SQL):** Deep-dive SQL queries answering specific retail performance questions.
4. **Excel Dashboard:** Programmatically generated multi-sheet workbook with Pivot Tables and KPIs.
5. **BI Integration:** Power BI schema and DAX documentation prepared for dashboarding.

## Key Performance Indicators (KPIs)
- Total Revenue & Total Profit
- Total Transactions & Units Sold
- Overall Profit Margin (%)
- Return Rate (%)

## Key Insights
1. **Pareto Principle:** The top 20% of products (mostly in the Electronics category) generate over 60% of the total net profit.
2. **Promotion Paradox:** While promotional campaigns successfully drive up total transaction volume, the heavy discounting leads to a lower overall profit margin compared to non-promotional periods.
3. **Return Rates:** Clothing and Apparel suffer from the highest return rates, negatively impacting net revenue for specific regional stores.

## Business Recommendations
- **Optimize Promotions:** Shift from flat-rate discounts to bundle offers to protect profit margins while still incentivizing higher transaction volumes.
- **Inventory Allocation:** Ensure high-margin Electronics are heavily stocked in the top 5 performing regional stores to maximize returns.
- **Reduce Returns:** Investigate sizing inconsistencies in the Clothing category and update online/in-store sizing guides to reduce the high return rate.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the python scripts in the `python/` folder sequentially to generate data, clean it, and output the Excel dashboard.
4. Review the SQL scripts in `sql/` and Power BI documentation in `powerbi/`.