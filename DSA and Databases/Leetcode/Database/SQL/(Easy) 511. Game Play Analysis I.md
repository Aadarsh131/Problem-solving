[511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/description/)

**MySql**

```sql
SELECT player_id, MIN(event_date) as first_login FROM Activity GROUP BY player_id
```