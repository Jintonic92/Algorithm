-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '%강원도%'
ORDER BY FACTORY_ID ASC

# SELECT ROUND(AVG(COALESCE(LENGTH, 10)), 2) AS 
# CASE WHEN THEN ELSE END
# DISTINCT
# FROM 
# JOIN ON
# WHERE
# GROUP BY
# HAVING
# ORDER BY
# LIMIT