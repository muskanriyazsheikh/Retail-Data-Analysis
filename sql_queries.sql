-- Total Sales by Region
SELECT region, Sum(sales) AS total_sales
FROM retail_data
GROUP BY  region;

-- Most profitable sub-category
SELECT sub_category, SUM(profit) AS total_profit
FROM retail_data
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 1;


