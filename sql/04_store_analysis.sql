-- Store Analysis
SELECT Store_Name, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Store_Name ORDER BY Total_Revenue DESC;
