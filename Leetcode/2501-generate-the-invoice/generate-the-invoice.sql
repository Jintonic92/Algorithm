# Write your MySQL query statement below
WITH BASE AS (
SELECT invoice_id
    -- , pur.product_id
    -- , quantity
    -- , price
    , sum(quantity * price) as total_price
FROM Purchases pur 
    LEFT JOIN Products pro ON pur.product_id = pro.product_id
GROUP BY 1
ORDER BY 2 DESC, 1
LIMIT 1
)
SELECT pur.product_id
    , pur.quantity
    , pro.price * pur.quantity as price
FROM Purchases pur 
    LEFT JOIN Products pro ON pur.product_id = pro.product_id
WHERE pur.invoice_id in (SELECT DISTINCT invoice_id FROM BASE)