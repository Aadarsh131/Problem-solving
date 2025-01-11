[184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/description/)

**MySql** (bruteforce sol)
```sql
WITH data AS (
    SELECT d.name as Department, MAX(e.salary) as salary FROM Employee e JOIN Department d ON departmentId=d.id GROUP BY departmentId
)
SELECT d.name as Department, e.name as Employee, e.salary as Salary FROM Employee e JOIN Department d ON (departmentId=d.id AND (d.name, e.salary) IN (SELECT Department, Salary FROM data))
```
- first take out all the `Department`, `Salary` (notice the casing) from `data` (i.e, all the max salary from each department). Consider the pair `(Department, Salary)` as the unique keys
- now use this pair to filter out all the `Employee`s 
- this will make sure all the people who have the maximum salary from each department gets shown
- Dont use `ORDER BY`, to match the testcases

**MySql** (optimal sol)
```sql
SELECT d.name as Department, e.name as Employee, e.salary as Salary FROM Employee e JOIN Department d ON (departmentId=d.id AND (salary, departmentId) IN (SELECT MAX(salary),departmentId FROM Employee GROUP BY departmentId)
)
```
- using subquery like this without using JOIN to filter out all the `Max(salary), departmentId` yields best performance
