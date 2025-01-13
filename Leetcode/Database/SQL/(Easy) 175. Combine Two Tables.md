[175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/description/)

**MySql**

```sql
SELECT firstName, lastName, city, state FROM Person p LEFT JOIN Address a ON p.personId=a.personId
```