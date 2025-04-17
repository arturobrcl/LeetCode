# Write your MySQL query statement below
DELETE person1
FROM Person person1
JOIN Person person2
ON person1.email = person2.email AND person1.id > person2.id;
