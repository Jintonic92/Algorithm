# Write your MySQL query statement below
SELECT IF(FROM_ID < TO_ID, FROM_ID, TO_ID) AS person1
    , IF(FROM_ID < TO_ID, TO_ID, FROM_ID) AS person2
    , COUNT(*) as call_count
    , SUM(duration) as total_duration
FROM CALLS T1
GROUP BY 1, 2
