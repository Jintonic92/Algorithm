# Write your MySQL query statement below

SELECT T1.name  AS Employee
FROM Employee T1
    LEFT JOIN Employee T2 ON T1.managerID = T2.id 
WHERE T1.salary > T2.salary