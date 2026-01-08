# Write your MySQL query statement below
WITH BASE AS (
SELECT E.email_id
    , user_id
    , signup_date
    , action_date
FROM emails E
    LEFT JOIN texts T ON E.email_id = T.email_id
WHERE signup_action = 'Verified'
)
SELECT user_id
-- SELECT *
--     , DATEDIFF(action_date, signup_date) 
FROM BASE
WHERE 1=1 
    AND CASE WHEN DATEDIFF(action_date, signup_date) = 1 THEN TRUE END 
ORDER BY 1 