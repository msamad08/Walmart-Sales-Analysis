-- Walmart Sales Analysis Queries

SELECT "Product line", ROUND(SUM(Total), 2) AS total_revenue
FROM sales
GROUP BY "Product line"
ORDER BY total_revenue DESC;

SELECT City, ROUND(SUM(Total), 2) AS total_revenue
FROM sales
GROUP BY City
ORDER BY total_revenue DESC;

SELECT "Customer type", ROUND(SUM(Total), 2) AS total_spent
FROM sales
GROUP BY "Customer type";

SELECT Payment, COUNT(*) AS transactions
FROM sales
GROUP BY Payment
ORDER BY transactions DESC;

SELECT strftime('%Y-%m', Date) AS month,
       ROUND(SUM(Total), 2) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;
