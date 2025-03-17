WITH first_order AS (
    SELECT customer_id, order_date, customer_pref_delivery_date, 
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_rank
    FROM Delivery
),
first_order_status AS (
    SELECT customer_id, order_date, customer_pref_delivery_date,
    CASE WHEN order_date = customer_pref_delivery_date THEN 'immediate' ELSE 'scheduled' END AS delivery_status
    FROM first_order
    WHERE order_rank = 1
)
SELECT 
ROUND(SUM(CASE WHEN delivery_status = 'immediate' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
AS immediate_percentage
FROM first_order_status;
