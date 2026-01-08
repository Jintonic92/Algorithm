# Write your MySQL query statement below

-- SELECT CEIL(DAYOFMONTH(purchase_date)/7) week_of_month 
--     , purchase_date
--     , SUM(amount_spend) AS total_amount
--     -- , CAST(DATE_FORMAT(purchase_date, '%w') AS UNSIGNED)
-- FROM Purchases
-- WHERE CAST(DATE_FORMAT(purchase_date, '%w') AS UNSIGNED) = 5 -- Friday
-- GROUP BY 1, 2
WITH RECURSIVE CAL AS(
    SELECT '2023-11-01' AS dates

    UNION ALL 

    SELECT DATE_ADD(dates, INTERVAL 1 DAY) AS dates
    FROM CAL 
    WHERE dates < '2023-11-30'
)
SELECT CEIL(DAYOFMONTH(CAL.dates)/7) AS week_of_month
    , CAL.dates as purchase_date
    , COALESCE(SUM(P.amount_spend), 0) as total_amount
FROM CAL    
    LEFT JOIN Purchases P ON P.purchase_date = CAL.dates
WHERE CAST(DATE_FORMAT(CAL.dates, '%w') AS UNSIGNED) = 5
GROUP BY 1, 2