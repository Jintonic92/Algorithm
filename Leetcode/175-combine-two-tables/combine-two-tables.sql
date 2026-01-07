# Write your MySQL query statement below

SELECT lastname
    , firstname
    , city
    , state
FROM PERSON P 
    LEFT JOIN ADDRESS A ON P.PERSONID = A.PERSONID