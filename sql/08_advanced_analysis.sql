-- Advanced SQL
WITH CustomerRank AS (
    SELECT Customer_ID, SUM(Revenue) as Total_Revenue,
    RANK() OVER(ORDER BY SUM(Revenue) DESC) as Rank
    FROM retail_sales GROUP BY Customer_ID
)
SELECT * FROM CustomerRank WHERE Rank <= 10;
