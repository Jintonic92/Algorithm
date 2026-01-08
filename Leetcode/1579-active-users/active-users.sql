# Write your MySQL query statement below
WITH BASE AS (
SELECT DISTINCT id
    , login_date
FROM Logins T1
)
, FINAL AS(
SELECT id
    , login_date
    , DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date) DAY) AS base_date
FROM BASE
)
SELECT DISTINCT F.id
    , A.name
FROM FINAL F
    JOIN Accounts A ON F.id = A.id
GROUP BY id, base_date
HAVING COUNT(*) >= 5
ORDER BY 1



