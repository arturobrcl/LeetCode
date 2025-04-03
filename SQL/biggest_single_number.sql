# Write your MySQL query statement below
WITH numbercount AS (
    SELECT num, SUM(num) AS sum, COUNT(num) AS count
    FROM MyNumbers
    GROUP BY num
)
SELECT MAX(num) AS num
FROM numbercount
WHERE num = sum AND count = 1 ;
