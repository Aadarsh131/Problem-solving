[627. Swap Salary](https://leetcode.com/problems/swap-salary/description/)

**MySql**
```sql
UPDATE Salary SET sex = 
CASE sex
    WHEN 'f' THEN  'm'
    ELSE 'f'
END;
```
*changes `sex` from `f` to `m` and vice-versa in a single `UPDATE` statement*