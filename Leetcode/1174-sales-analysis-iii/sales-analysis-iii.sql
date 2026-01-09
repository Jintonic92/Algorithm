# Write your MySQL query statement below
WITH FILTER AS (
    SELECT S.product_id
    FROM Sales S 
    WHERE 1=1 
        AND sale_date >= '2019-04-01' OR sale_date < '2019-01-01'
)
SELECT P.product_id
    , P.product_name
FROM Product P
    LEFT JOIN Sales S ON S.product_id = P.product_id
WHERE P.product_id NOT IN (SELECT DISTINCT product_id FROM FILTER)
    AND S.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY 1, 2