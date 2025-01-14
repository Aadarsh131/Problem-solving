[1158. Market Analysis I](https://leetcode.com/problems/market-analysis-i/description/)

**MySql**

```sql
SELECT user_id as buyer_id, join_date, COUNT(order_id) orders_in_2019
FROM Users LEFT JOIN Orders
ON user_id=buyer_id AND YEAR(order_date)='2019'
GROUP BY user_id, join_date
```
- `AND` on the `ON` makes sure the join only happens for the  `2019` orders
  
OR
```sql
WITH filtered_orders AS (
    SELECT order_date, buyer_id FROM Orders WHERE order_date LIKE '2019%'
)

SELECT user_id as buyer_id, join_date, 
COUNT(buyer_id) as orders_in_2019
FROM Users LEFT JOIN filtered_orders
ON user_id=buyer_id
GROUP BY user_id, join_date
```
### Bad code
```sql
SELECT user_id as buyer_id, join_date, 
SUM(CASE WHEN order_date LIKE '2019%' THEN 1 ELSE 0 END) as orders_in_2019
FROM Users LEFT JOIN Orders
ON user_id=buyer_id
GROUP BY user_id, join_date
```
- it is joining the whole tables first before checking for `2019` rows, increasing the time complexity

### Understanding a concept

Why do this code doesn't work?
```sql
SELECT u.user_id AS buyer_id,join_date,
SUM(CASE WHEN o.order_id is NULL THEN 0 ELSE 1 END) AS orders_in_2019
FROM Users u LEFT JOIN Orders o ON u.user_id = o.buyer_id
WHERE o.order_date is NULL OR year(o.order_date) ='2019'
GROUP BY u.user_id;
```
Everthing looks fine with the code, but the condition `o.order_date is NULL` is never going to met. 

>**Reason**-  in a `LEFT JOIN`, filtering in the `WHERE` clause can turn the join into an `INNER JOIN` by removing rows where the right-side table is `NULL`.

Solution-
```sql
SELECT u.user_id AS buyer_id,join_date,
SUM(CASE WHEN o.order_id is NULL THEN 0 ELSE 1 END) AS orders_in_2019
FROM Users u LEFT JOIN Orders o ON u.user_id = o.buyer_id AND year(o.order_date) ='2019'
GROUP BY u.user_id;
```