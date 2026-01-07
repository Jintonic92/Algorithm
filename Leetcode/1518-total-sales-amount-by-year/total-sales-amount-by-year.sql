# Write your MySQL query statement below
WITH RECURSIVE years as(
    SELECT year(MIN(PERIOD_START)) as year 
    FROM SALES 

    UNION ALL 

    SELECT year + 1 
    FROM years
    WHERE year < 2020


)

SELECT s.product_id
    , product_name
    , CAST(year AS CHAR) as report_year
    , (DATEDIFF(LEAST(s.period_end, DATE(CONCAT(y.year, '-12-31'))),
                GREATEST(s.period_start, DATE(CONCAT(y.year, '-01-01')))
    ) + 1 ) * average_daily_sales as total_amount
    -- , (DATEDIFF(
    --     LEAST(s.period_end, DATE(CONCAT(y.report_year, '-12-31'))), 
    --     GREATEST(s.period_start, DATE(CONCAT(y.report_year, '-01-01')))
    -- ) + 1) * s.average_daily_sales AS total_amount
FROM Sales s
    LEFT JOIN Product p ON p.product_id = s.product_id
    JOIN years y ON y.year between YEAR(period_start) and YEAR(period_end)
GROUP BY 1, 2, 3
ORDER BY 1, 3
