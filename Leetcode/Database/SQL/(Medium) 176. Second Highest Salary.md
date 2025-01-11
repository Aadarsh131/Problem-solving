[176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/)

**MySql**

```sql
SELECT (
    SELECT DISTINCT salary 
    FROM Employee 
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1    
) as SecondHighestSalary
```
- subquery is a `scalar subquery` returning only one value, `NULL` if it returns nothing.   
  This is the reason we see `NULL` instead of an **Empty table**
- `Subquery returns more than 1 row` this error would be shown if the scalar subquery returns more than 1 value (eg. when, `LIMIT` is set to value  `>1`)