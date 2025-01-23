[608. Tree Node](https://leetcode.com/problems/tree-node/description)

**MySql**
```sql
SELECT id, 
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END as type
FROM Tree
```
> **NOTE**: we need `WHERE p_id IS NOT NULL` to ensure the following  

```sql
id NOT IN (NULL, 1, 2)
```
If `NULL` is in the list, any comparison involving `NULL` results in `NULL` (not `True` or `False`)

As a result, `id NOT IN` returns `FALSE` for every row, even for values `3`, `4`, and `5` which should have been 'Leaf'


### OR Simply
**MySql**
```sql
SELECT id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree)THEN 'Inner'
        ELSE 'Leaf'
        END AS type
 FROM Tree
```