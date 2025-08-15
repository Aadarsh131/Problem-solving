[The Blunder](https://www.hackerrank.com/challenges/the-blunder/problem)

**MySql**
```sql
SELECT CEIL(AVG(Salary)- AVG(REPLACE(Salary,'0',''))) FROM EMPLOYEES
```

- can also use `REGEXP_REPLACE()`