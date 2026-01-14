# Write your MySQL query statement below
WITH timediffs AS(
SELECT machine_id,
process_id,
activity_type,
timestamp - LAG(timestamp) OVER (PARTITION BY machine_id, process_id ORDER BY timestamp) AS timediff
FROM activity
ORDER BY machine_id ASC, process_id ASC, activity_type ASC, timestamp ASC)


SELECT machine_id, ROUND(SUM(timediff)/COUNT(DISTINCT process_id),3) AS 'processing_time'
FROM timediffs
WHERE activity_type = 'end'
GROUP BY machine_id;
