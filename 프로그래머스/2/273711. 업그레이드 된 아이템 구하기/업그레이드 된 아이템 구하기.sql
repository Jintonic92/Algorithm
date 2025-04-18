-- 코드를 작성해주세요
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IN (
    SELECT ITEM_ID
    FROM ITEM_INFO 
    WHERE RARITY = 'RARE'
)
ORDER BY I.ITEM_ID DESC



# SELECT T.ITEM_ID, I.ITEM_NAME, I.RARITY
# FROM ITEM_INFO I JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
# WHERE T.PARENT_ITEM_ID IN(
#     SELECT ITEM_ID
#     FROM ITEM_INFO
#     WHERE RARITY = 'RARE'
# )
# ORDER BY T.ITEM_ID DESC


# SELECT CEIL(AVG(COALESCE(LENGTH, 10))) AS
# DISTINCT(COUNT) AS
# CASE WHEN THEN ELSE END AS
# FROM JOIN ON
# WHERE GROUP BY HAVING ORDER BY LIMIT