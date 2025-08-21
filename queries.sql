-- ============================
-- Sales & Operations Dashboard SQL Queries
-- ============================

-- 1. Total Sales by Region
SELECT region, SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;

-- 2. Monthly Sales Trend
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(sales_amount) AS monthly_sales
FROM sales_data
GROUP BY month
ORDER BY month;

-- 3. Operational Efficiency by Region
SELECT region,
       (SUM(successful_ops) * 100.0 / NULLIF(SUM(total_ops),0)) AS efficiency_percentage
FROM operations_data
GROUP BY region
ORDER BY efficiency_percentage DESC;

-- 4. Top 5 Products by Sales
SELECT product_name, SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

-- 5. Sales vs Operations Join
SELECT s.region,
       SUM(s.sales_amount) AS total_sales,
       (SUM(o.successful_ops) * 100.0 / NULLIF(SUM(o.total_ops),0)) AS efficiency
FROM sales_data s
JOIN operations_data o ON s.region = o.region
GROUP BY s.region
ORDER BY total_sales DESC;
