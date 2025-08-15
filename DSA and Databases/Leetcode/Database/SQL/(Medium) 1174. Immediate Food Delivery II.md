[1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/description/)

**MySql**

*Bruteforce solution*:
> Time complexity: $O(2n)$  
> Space complexity: 
```sql
SELECT ROUND(SUM(IF(order_date=customer_pref_delivery_date,1,0))/COUNT(*) *100,2) as immediate_percentage FROM (
    SELECT *, RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as rn
    FROM Delivery
) as cte
WHERE rn=1
```
*Optimal solution*:
> Time complexity: $O(n)$   
> Space complexity:
```sql
Select round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);
```