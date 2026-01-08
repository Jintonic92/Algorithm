# Write your MySQL query statement below
WITH BASE AS (
SELECT server_id
    , status_time
    , session_status
    , LEAD(status_time) OVER(PARTITION BY server_id ORDER BY status_time) AS next_time
FROM Servers
)
SELECT FLOOR(SUM(TIMESTAMPDIFF(SECOND, status_time, next_time)/24/60/60)) AS total_uptime_days
FROM BASE 
WHERE session_status = 'start'
