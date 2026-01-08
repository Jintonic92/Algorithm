# Write your MySQL query statement below
WITH BASE AS (
SELECT buyer_id
    , count(order_id) as cnt
FROM Orders
WHERE YEAR(order_date) = 2019
GROUP BY 1
)
SELECT U.user_id AS buyer_id
    , U.join_date 
    , COALESCE(cnt, 0) AS orders_in_2019
FROM Users U
    LEFT JOIN BASE B ON U.user_id = B.buyer_id