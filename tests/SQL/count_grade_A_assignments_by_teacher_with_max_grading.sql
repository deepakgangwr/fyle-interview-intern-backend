-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH CTE AS(
    SELECT teacher_id, COUNT(*) AS number_of_assignments FROM assignments GROUP BY teacher_id
)
SELECT COUNT(*) as number_of_grade_A_assignments, teacher_id FROM assignments
WHERE grade = 'A' AND teacher_id = (SELECT teacher_id FROM CTE ORDER BY number_of_assignments DESC LIMIT 1)