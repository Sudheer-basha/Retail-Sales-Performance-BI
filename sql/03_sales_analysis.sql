-- Sales Analysis
SELECT DATE_TRUNC('month', Transaction_Date) as Month, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY 1 ORDER BY 1;
