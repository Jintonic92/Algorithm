# Write your MySQL query statement below
WITH POS AS (
SELECT patient_id
    , min(test_date) as first_pos
FROM covid_tests
WHERE result = 'POSITIVE'
GROUP BY 1
)
, BASE AS( 
SELECT C.patient_id
    , first_pos
    , min(test_date) as last_neg
FROM covid_tests C
    JOIN POS ON C.patient_id = POS.patient_id AND first_pos < test_date
WHERE result = 'NEGATIVE'
GROUP BY 1
)
SELECT P.patient_id
    , patient_name
    , age
    , DATEDIFF(last_neg, first_pos) AS recovery_time
FROM BASE B
    LEFT JOIN patients P ON P.patient_id = B.patient_id 
ORDER BY 4, 2

-- WITH BASE AS (
-- SELECT patient_id
--     , result AS first_result
--     , test_date AS first_date
--     , LEAD(result) OVER(PARTITION BY patient_id ORDER BY test_date) AS next_result
--     , LEAD(test_date) OVER(PARTITION BY patient_id ORDER BY test_date) AS next_date
-- FROM covid_tests c
-- WHERE result IN ('Positive', 'Negative')
-- )
-- SELECT B.patient_id
--     , patient_name
--     , age 
--     , DATEDIFF(next_date, first_date) AS recovery_time
-- FROM BASE B
--     LEFT JOIN patients P ON P.patient_id = B.patient_id 
-- WHERE 1=1 
--     AND first_result = 'Positive' 
--     AND next_result = 'Negative'
-- ORDER BY 4, 2

