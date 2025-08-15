[The Report](https://www.hackerrank.com/challenges/the-report/problem)

**MySql** 
```sql
SELECT 
    IF(Grade < 8, NULL,Name), Grade, Marks
FROM Students s JOIN Grades g
ON s.marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY Grade DESC,
    CASE WHEN Grade < 8 THEN  Marks ELSE Name END
```