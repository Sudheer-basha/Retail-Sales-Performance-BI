-- Data Quality Checks
SELECT COUNT(*) FROM retail_sales WHERE Customer_ID IS NULL;
SELECT COUNT(*) FROM retail_sales WHERE Quantity < 0;
