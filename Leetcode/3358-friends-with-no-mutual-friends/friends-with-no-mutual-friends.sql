# Write your MySQL query statement below
WITH BASE AS( 
    SELECT user_id1 AS u1
        , user_id2 AS u2
    FROM Friends F

    UNION

    SELECT user_id2 AS u1
        , user_id1 AS u2
    FROM Friends F

)
SELECT user_id1
    , user_id2
FROM Friends F
WHERE NOT EXISTS ( SELECT 1 
                    FROM BASE B1 
                        JOIN BASE B2 ON B1.u2 = B2.u2 -- 공통친구
                    WHERE F.user_id1 = B1.u1 AND F.user_id2 = B2.u1
) 
ORDER BY 1, 2