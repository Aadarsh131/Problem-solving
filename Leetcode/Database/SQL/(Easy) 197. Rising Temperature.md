[197. Rising Temperature](https://leetcode.com/problems/rising-temperature/description/)

**MySql**

```sql
WITH cte AS (SELECT CASE WHEN ((LAG(temperature,1) OVER() < temperature) AND LAG(recordDate,1) OVER() = DATE_SUB(recordDate, INTERVAL 1 DAY)) THEN id END as Id FROM Weather ORDER BY recordDate)

SELECT * FROM cte WHERE id IS NOT NULL
```
- don't use `date = date - 1` approach (as `DATE('2020-05-01') - 1` = `('2020-05-00')`, which is wrong), use `DATE_SUB()` instead