[181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/)

**MySql**
```sql
SELECT e1.name as Employee
FROM Employee e1 JOIN Employee e2
ON (e1.managerID=e2.id AND e1.salary > e2.salary)
```