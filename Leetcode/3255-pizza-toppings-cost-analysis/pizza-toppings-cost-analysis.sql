# Write your MySQL query statement below
SELECT CONCAT(T1.topping_name, ',', T2.topping_name, ',', T3.topping_name) as pizza
    , T1.cost + T2.cost + T3.cost as total_cost
FROM Toppings T1
    JOIN Toppings T2 ON T1.topping_name < T2.topping_name
    JOIN Toppings T3 ON T2.topping_name < T3.topping_name
ORDER BY 2 DESC, 1 

