# Write your MySQL query statement below
WITH BASE AS (
SELECT candidate_id
    , GROUP_CONCAT(skill) AS skill
FROM Candidates 
-- WHERE skill in ('Python', 'Tableau', 'PostgreSQL')
GROUP BY 1
) 
SELECT candidate_id
FROM BASE
WHERE skill like '%Python%'
    AND skill like '%Tableau%'
    AND skill like '%PostgreSQL%'
ORDER BY 1 