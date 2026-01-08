# Write your MySQL query statement below
WITH BASE AS( 
SELECT account_id
    , day
    , CASE WHEN type = 'Deposit' Then amount ELSE -amount END amount 
FROM Transactions
)
SELECT account_id
    , day
    , SUM(amount) OVER(PARTITION BY account_id ORDER BY day) as balance
FROM BASE
