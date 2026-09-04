-- Customer Analysis
SELECT Customer_Type, COUNT(DISTINCT Customer_ID) as Unique_Customers, SUM(Revenue) as Total_Revenue
FROM retail_sales GROUP BY Customer_Type;
