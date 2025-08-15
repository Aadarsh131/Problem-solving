[Average Population](https://www.hackerrank.com/challenges/average-population/)

**MySql**

```sql
SELECT CAST(AVG(POPULATION) AS UNSIGNED) FROM CITY
ORDER BY NAME
```
- casting to integers can be done with `CAST(value AS SIGNED)` or `CAST(value AS UNGIGNED)`