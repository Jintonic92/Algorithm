-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
COALESCE(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '%경기도%'
ORDER BY WAREHOUSE_ID ASC

# SELECT ROUND(AVG(COALESCE(LENGTH, 10)), 2) AS 
# CASE WHEN THEN ELSE END AS
# DISTINCT
# FROM 
# JOIN ON 
# WHERE
# GROUP BY
# HAVING
# ORDER BY
# DISTINCT