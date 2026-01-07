# Write your MySQL query statement below
WITH BASE AS( 
SELECT exam_id
    , MAX(score) as max_score
    , MIN(score) as min_score
FROM Exam 
GROUP BY 1
)
, FINAL AS( 
SELECT E.student_id
    , COUNT(case when score = max_score or score = min_score then 1 end) as something
FROM Exam E 
    LEFT JOIN BASE B ON E.exam_id = B.exam_id
GROUP BY student_id
ORDER BY E.exam_id
)
SELECT F.student_id
    , student_name
FROM FINAL F
    LEFT JOIN Student S ON F.student_id = S.student_id
WHERE something = 0 
ORDER BY 1
