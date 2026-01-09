# Write your MySQL query statement below
SELECT P.product_id
    , COALESCE(ROUND(SUM(price * units) / sum(units), 2), 0) AS average_price
FROM PRICES P
    LEFT JOIN UnitsSold U ON U.purchase_date BETWEEN P.start_date AND P.end_date and P.product_id = U.product_id
GROUP BY 1