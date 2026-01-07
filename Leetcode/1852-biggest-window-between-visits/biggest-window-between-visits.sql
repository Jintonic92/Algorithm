# Write your MySQL query statement below
WITH BASE AS(
SELECT user_id
    , visit_date
    , LEAD(VISIT_DATE, 1, '2021-01-01') OVER(PARTITION BY user_id ORDER BY visit_date) as lead_date
FROM UserVisits
)
SELECT user_id
    , MAX(DATEDIFF(lead_date, visit_date)) as biggest_window
FROM BASE
GROUP BY 1
