[177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/description/)

**MySql**

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    with salary_rows AS (
        SELECT DISTINCT salary, ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num FROM Employee GROUP BY salary
    )
    SELECT salary FROM salary_rows WHERE row_num=N
  );
END
```
- `salary` gets its speical `group by`, because with ROW_NUMBER() column by its side, `DISTINCT` doesn't really shows the distinct values by `salary`, it shows the distict values with ROW_NUMBER() which is essentially all of the rows as each ROW_NUMBER() is always different here because we have NOT `PARTITION BY` it by any value
