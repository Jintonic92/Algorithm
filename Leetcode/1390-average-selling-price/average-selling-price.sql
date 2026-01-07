# Write your MySQL query statement below
SELECT p.product_id
    , IFNULL(ROUND(sum(price * units) / sum(units), 2), 0) as average_price
FROM PRICES P
    LEFT JOIN unitssold U ON P.PRODUCT_ID = U.PRODUCT_ID 
        AND PURCHASE_DATE BETWEEN START_DATE AND END_DATE
GROUP BY 1