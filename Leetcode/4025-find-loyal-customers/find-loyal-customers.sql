# Write your MySQL query statement below
WITH BASE AS (
SELECT customer_id
    , DATEDIFF(MAX(transaction_date), MIN(transaction_date)) + 1 as date_diff
    , COALESCE(SUM(CASE WHEN transaction_type = 'refund' THEN 1 END)/COUNT(transaction_id), 0) as refund_rate
FROM customer_transactions
GROUP BY customer_id
HAVING COUNT(transaction_id) >= 3 
) 
SELECT customer_id
FROM BASE
WHERE date_diff > 30 
AND refund_rate < 0.2
