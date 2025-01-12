[577. Employee Bonus](https://leetcode.com/problems/employee-bonus/description/)

**MySql**
```sql
select name, bonus from Employee e left join Bonus b ON e.empId=b.empId where bonus < 1000 or bonus is null
```