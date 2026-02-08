# Write your MySQL query statement below
SELECT ROUND(SUM(immediate)/COUNT(immediate) * 100, 2) AS immediate_percentage
FROM (
    SELECT IF(MIN(order_date) = MIN(customer_pref_delivery_date), 1, 0) AS immediate
    FROM Delivery
    GROUP BY customer_id
    ) AS subquery_table;
