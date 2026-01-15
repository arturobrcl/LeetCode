# Write your MySQL query statement below
WITH student_subject AS(
    SELECT s.student_id, s.student_name, u.subject_name AS subject FROM Students s
    CROSS JOIN Subjects u
)
SELECT s.student_id, s.student_name, s.subject AS subject_name, SUM(IF(e.subject_name = s.subject, 1, 0)) AS attended_exams
FROM student_subject s
LEFT JOIN Examinations e
ON e.student_id = s.student_id
GROUP BY s.student_id, s.student_name, s.subject
ORDER BY s.student_id ASC, s.subject ASC;
