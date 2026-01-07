# Write your MySQL query statement below
WITH BASE AS (
SELECT B.box_id
    , B.chest_id
    , b.apple_count b_apple
    , COALESCE(c.apple_count, 0) c_apple
    , b.orange_count b_orange
    , COALESCE(c.orange_count, 0) c_orange
FROM BOXES B
    LEFT JOIN CHESTS C ON B.chest_id = c.chest_id
)
SELECT SUM(b_apple + c_apple) as apple_count 
    , SUM(b_orange + c_orange) as orange_count
FROM BASE