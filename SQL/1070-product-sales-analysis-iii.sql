# Write your MySQL query statement below
WITH min_year (product_id, first_year, price) AS (
    SELECT product_id, MIN(year) AS first_year, price
    FROM Sales
    GROUP BY product_id
)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN min_year AS m
    ON s.product_id = m.product_id
    AND s.year       = m.first_year;;
