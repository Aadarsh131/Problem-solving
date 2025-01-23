[1393. Capital Gain/Loss](https://leetcode.com/problems/capital-gainloss/description)

**MySql**

```sql
SELECT stock_name, SUM(if(operation='Sell',price ,-price)) as capital_gain_loss
FROM Stocks 
GROUP BY stock_name
```