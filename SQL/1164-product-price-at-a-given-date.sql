WITH pre_table AS (
SELECT product_id, new_price AS price
FROM (
    SELECT
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY change_date ASC
        ) AS row_num,
        COUNT(*) OVER (PARTITION BY product_id) AS cnt_rows
    FROM Products
    WHERE change_date <= '2019-08-16'
) AS t
WHERE row_num = cnt_rows),

post_table AS (
    SELECT product_id, price
    FROM (
        SELECT
            product_id,
            10 AS price,
            change_date,
            ROW_NUMBER() OVER (
                PARTITION BY product_id
                ORDER BY change_date DESC
            ) AS row_num,
            COUNT(*) OVER (PARTITION BY product_id) AS cnt_rows
        FROM Products
        WHERE change_date >= '2019-08-16'
    ) AS t
    WHERE row_num = cnt_rows AND product_id NOT IN (SELECT product_id FROM pre_table)
)

SELECT * FROM pre_table
UNION 
SELECT * FROM post_table; 
