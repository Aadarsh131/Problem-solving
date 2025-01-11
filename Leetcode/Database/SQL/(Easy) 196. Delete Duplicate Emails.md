[196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/)

**MySql**

```sql
WITH finalPeople AS (
    SELECT id
    FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_num
        FROM Person
    ) ranked
    WHERE row_num = 1
)
DELETE FROM Person
WHERE id NOT IN (SELECT id FROM finalPeople);
```

Easy way using self join
```sql
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;
```