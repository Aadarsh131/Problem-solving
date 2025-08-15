[182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/)

**MySql**

```sql
SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1
```