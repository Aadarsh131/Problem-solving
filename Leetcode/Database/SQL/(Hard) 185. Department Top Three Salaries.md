[185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/)

**MySql**

```sql
with emp_with_rank as (
    select *, dense_rank() over(partition by departmentId order by salary desc) as rnk from Employee
)

select d.name as Department, e.name as Employee, salary from emp_with_rank e join Department d 
on departmentId=d.id 
where rnk <= 3
```