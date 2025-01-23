[Higher Than 75 Marks](https://www.hackerrank.com/challenges/more-than-75-marks/)

**MySql**

```sql
SELECT name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(Name, 3), id
```
- `RIGHT(Name, 3)` extracts out `3` char from `Name` from right