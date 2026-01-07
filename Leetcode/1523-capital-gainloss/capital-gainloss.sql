# Write your MySQL query statement below
-- WITH BASE AS (
-- SELECT stock_name
--     , operation
--     , price
--     , LEAD(price) OVER(PARTITION BY stock_name ORDER BY operation_day ) lead_price
-- FROM Stocks
-- )
-- SELECT stock_name
--     , sum(lead_price - price) as capital_gain_loss
-- FROM BASE
-- WHERE operation = 'Buy'
-- GROUP BY 1

SELECT stock_name
    , SUM(CASE WHEN operation = 'Sell' then price else -price END) as capital_gain_loss
FROM Stocks
GROUP BY 1