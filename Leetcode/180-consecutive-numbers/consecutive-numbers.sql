# Write your MySQL query statement below
-- Time limit exceeded
-- WITH BASE AS (
-- SELECT num
--     , LAG(num, 1) OVER(ORDER BY id) as prev
--     , LAG(num, 2) OVER(ORDER BY id) as prev_prev
-- FROM Logs 
-- )
-- SELECT DISTINCT num as ConsecutiveNums
-- FROM BASE
-- WHERE num = prev AND prev = prev_prev

SELECT DISTINCT T1.num as ConsecutiveNums
FROM Logs T1
    JOIN Logs T2 ON T1.id = T2.id - 1
    JOIN Logs T3 ON T2.id = T3.id - 1
WHERE T1.num = T2.num AND T2.num= T3.num