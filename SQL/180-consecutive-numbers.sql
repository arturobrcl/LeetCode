# Write your MySQL query statement below
WITH CTE AS (SELECT id, num, prev, SUM(CASE WHEN num = prev THEN 0 ELSE 1 END) OVER(ORDER BY id) AS grp
FROM (
    SELECT *,
    LAG (num, 1) 
    OVER (ORDER BY id) AS prev
    FROM Logs
) AS t)

SELECT DISTINCT num AS ConsecutiveNums
FROM CTE
GROUP BY num, grp
HAVING COUNT(grp) >= 3;
