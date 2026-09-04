-- Product Analysis
SELECT Product_Name, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Product_Name ORDER BY Total_Revenue DESC;
