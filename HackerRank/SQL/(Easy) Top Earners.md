[Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees/problem)

**MySql**

```sql
SELECT MAX(salary * months) AS total_salary, COUNT(*) AS count
FROM Employee
WHERE salary * months = (SELECT MAX(salary * months) FROM Employee);
```
- NOTE- we used `MAX(salary * months) AS total_salary` just to extract out 1 value, as when combied with `COUNT(*)`(which aggregates the value)
just any column would give an indeterministic output or if not an error
