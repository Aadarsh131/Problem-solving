[1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/description/)

**MySql**
```sql
SELECT user_id, ROUND(IFNULL(confirmation_rate,0),2) as confirmation_rate
FROM Signups LEFT JOIN (
    SELECT user_id, SUM(IF(action='confirmed',1,0))/COUNT(action) as confirmation_rate 
    FROM Confirmations
    GROUP BY user_id
) AS rates
USING(user_id)
```