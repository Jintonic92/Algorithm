# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers C
    LEFT JOIN Orders O ON C.id = O.customerID
WHERE O.id IS NULL