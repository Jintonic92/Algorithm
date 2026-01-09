# Write your MySQL query statement below
WITH BASE AS (
SELECT departmentId
    , salary
    , ROW_NUMBER() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rn
FROM Employee
GROUP BY 1, 2
)

SELECT D.name as Department
    , E.name as Employee
    , E.salary as Salary
FROM Employee E 
    JOIN BASE B ON E.departmentId = B.departmentId AND E.salary = B.salary 
    JOIN Department D ON D.id = B.departmentId
WHERE rn <= 3