-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 20
ORDER BY HOUR


# SELECT ROUND(AVG(COALESCE(LENGTH, 10)), 2) AS 
# COUNT(DISTINCT NAME) AS
# DISTINCT 
# FROM JOIN ON
# WHERE
# GROUP BY
# HAVING
# ORDER BY
# LIMIT