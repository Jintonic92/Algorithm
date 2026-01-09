# Write your MySQL query statement below
WITH BASE AS (
    SELECT parent_id as post_id
        , COUNT(DISTINCT sub_id) as number_of_comments
    FROM Submissions 
    GROUP BY 1
)
SELECT sub_id AS post_id
    , COALESCE(number_of_comments, 0) AS number_of_comments
FROM Submissions S
    LEFT JOIN BASE B ON S.sub_id = B.post_id
WHERE S.parent_id IS NULL
GROUP BY 1, 2
ORDER BY 1
