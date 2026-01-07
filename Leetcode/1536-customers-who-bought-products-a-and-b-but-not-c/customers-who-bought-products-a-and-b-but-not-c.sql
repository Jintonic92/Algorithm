# Write your MySQL query statement below
-- WITH BASE AS (
-- SELECT customer_id
--     , GROUP_CONCAT(distinct product_name) grouped
-- FROM Orders
-- GROUP BY 1
-- ) 
-- SELECT Base.customer_id
--     , C.customer_name
-- FROM BASE
--     JOIN Customers C on BASE.customer_id = C.customer_id
-- WHERE 

SELECT c.customer_id  
    , customer_name
FROM Customers C
    LEFT JOIN Orders O ON C.customer_id = O.customer_id 
GROUP BY 1, 2 
HAVING SUM(product_name = 'A') > 0
    AND SUM(product_name = 'B') > 0
    AND SUM(product_name = 'C') = 0 
    