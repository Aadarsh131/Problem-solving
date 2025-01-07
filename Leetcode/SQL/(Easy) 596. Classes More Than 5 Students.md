[596. Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/description/)


```
Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+

Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+
```
**MySql**
```sql
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5
```

