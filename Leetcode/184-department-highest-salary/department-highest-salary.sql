# Write your MySQL query statement below

WITH BASE AS (
SELECT departmentId
    , MAX(salary) as max_salary
FROM Employee
GROUP BY 1
)

SELECT
     D.name as Department
    , E.name as Employee
    , salary as Salary
FROM Employee E 
        JOIN BASE B ON E.departmentId = B.departmentId AND B.max_salary = E.salary
        JOIN Department D ON D.id = E.departmentID  