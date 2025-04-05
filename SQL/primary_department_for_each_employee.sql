# Write your MySQL query statement below
WITH EmployeeCounts AS (
    SELECT employee_id, COUNT(*) as cnt
    FROM Employee
    GROUP BY employee_id
)
SELECT e.employee_id, e.department_id
FROM Employee e
LEFT JOIN EmployeeCounts ec ON e.employee_id = ec.employee_id
WHERE e.primary_flag = 'Y' OR ec.cnt = 1;
