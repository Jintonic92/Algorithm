# Write your MySQL query statement below
WITH BASE AS( 
    SELECT car_id

        , SUM(fee_paid) as total_fee_paid
        , ROUND(SUM(fee_paid)/SUM((TIMESTAMPDIFF(MINUTE, entry_time, exit_time)/60)), 2)as avg_hourly_fee
    FROM ParkingTransactions 
    GROUP BY 1
    ORDER BY 1, 3 DESC
)
, FILTER AS(
    SELECT car_id
        , lot_id
        , SUM((TIMESTAMPDIFF(MINUTE, entry_time, exit_time)/60)) AS time_diff   
        , ROW_NUMBER() OVER(PARTITION BY car_id ORDER BY SUM((TIMESTAMPDIFF(MINUTE, entry_time, exit_time)/60)) DESC) AS RN
    FROM ParkingTransactions
    GROUP BY 1, 2
)
SELECT F.car_id
    , total_fee_paid
    , avg_hourly_fee
    , lot_id as most_time_lot
FROM FILTER F
    LEFT JOIN BASE B ON F.car_id = B.car_id
WHERE RN = 1