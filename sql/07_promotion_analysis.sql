-- Promotion Analysis
SELECT Promotion, SUM(Revenue) as Total_Revenue, SUM(Discount) as Total_Discount
FROM retail_sales GROUP BY Promotion;
