[596. Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/description/)

**MySql**
```sql
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5
```
*returns only those column `class` from table `Courses` whose `student` count (no. of student in a class) is `>=` 5*


