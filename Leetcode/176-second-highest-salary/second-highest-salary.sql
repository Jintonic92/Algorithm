# Write your MySQL query statement below

WITH BASE AS (
SELECT DISTINCT salary
    , DENSE_RANK() OVER(ORDER BY SALARY DESC) rn
FROM Employee
ORDER BY 2 DESC
)
SELECT max(salary) as SecondHighestSalary
FROM BASE
WHERE rn = 2