[626. Exchange Seats](https://leetcode.com/problems/exchange-seats/description/)

# Intuition and Approach 1
Dont change the order of the `id` (as it is already sorted), just swap the `student` names for every two consecutive rows (takes $O(n)$ time)

> Time Complexity- $O(n)$ (traverses the table only once)

```sql
SELECT id,
    CASE 
        WHEN MOD(id,2)=0 THEN LAG(student,1) OVER()
        ELSE COALESCE(LEAD(student,1) OVER(), student)
    END as student
FROM Seat
```

# Intuition and Approach 2
1. Just swap the row for every two consecutive rows (take $O(n)$ time)
2. then assign the row numbers to it from a newly created column (takes $O(n)$ time) 

> Time Complexity- $O(n) + O(n) = O(2n) \approx O(n)$  (traverses the table 2 times)

```sql
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)
```