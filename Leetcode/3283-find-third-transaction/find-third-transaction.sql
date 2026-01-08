# Write your MySQL query statement below
WITH BASE AS (
SELECT user_id
    , spend
    , transaction_date 
    , ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY transaction_date) AS rn
    , LAG(spend, 1) OVER(PARTITION BY user_id ORDER BY transaction_date) AS prev
    , LAG(spend, 2) OVER(PARTITION BY user_id ORDER BY transaction_date) AS prev_prev
FROM Transactions T
)
SELECT user_id
    , spend AS third_transaction_spend 
    , transaction_date AS third_transaction_date 
FROM BASE
WHERE 1=1 
    AND rn = 3
    AND spend > prev
    AND spend > prev_prev


