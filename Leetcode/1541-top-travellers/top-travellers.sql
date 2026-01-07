# Write your MySQL query statement below
SELECT name
    , SUM(COALESCE(distance, 0)) as travelled_distance
FROM Users U 
    LEFT JOIN Rides R On R.user_id = U.id
GROUP BY name, U.id
ORDER BY 2 DESC, 1 