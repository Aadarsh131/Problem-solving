[262. Trips and Users](https://leetcode.com/problems/trips-and-users/description/)

**MySql**
```sql
SELECT request_at as Day, ROUND((SUM(CASE WHEN status IN ('cancelled_by_driver','cancelled_by_client') THEN 1 ELSE 0 END)/COUNT(status)),2) AS `Cancellation Rate` FROM Trips 
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes')
AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes')
AND request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY request_at
```
- suggestion- dont use JOIN here as it will create multiple rows, which would make out final calculation logic tougher