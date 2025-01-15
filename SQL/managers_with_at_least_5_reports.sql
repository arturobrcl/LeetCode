# Write your MySQL query statement below
SELECT e2.name
FROM Employee e1
JOIN Employee e2
ON e1.managerID = e2.id
GROUP BY e1.managerID
HAVING COUNT(e1.managerID) >= 5;