# Write your MySQL query statement below
# Order by turn and get total weight
# First index where sum greater 1000, return prev val

# Write your MySQL query statement below
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;

-- 1204_last_person_to_fit_on_the_bus.sql
