[595. Big Countries](https://leetcode.com/problems/big-countries/)

**MySql**
```sql
SELECT name, population, area FROM WORLD WHERE area >= 3000000 OR population >= 25000000
```