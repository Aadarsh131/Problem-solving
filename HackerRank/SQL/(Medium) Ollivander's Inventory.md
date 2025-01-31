[Ollivander's Inventory](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem)

**MySql**
```sql
SELECT id, age, cte.coins_needed, cte.power
FROM Wands w1 JOIN (
    SELECT code, age, MIN(coins_needed) as coins_needed, power
    FROM Wands JOIN Wands_property 
    using (code)
    WHERE is_evil = 0
    GROUP BY code, age, power
    ) as cte
using(coins_needed,code)
ORDER BY cte.power DESC, cte.age DESC
```