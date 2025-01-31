[Contest Leaderboard](https://www.hackerrank.com/challenges/contest-leaderboard/problem)

**MySql**
```sql
SELECT a.hacker_id, name,  total_score 
FROM 
    Hackers as a 
    JOIN (
        SELECT hacker_id, SUM(maxi_score) as total_score 
        FROM (
            SELECT 
                hacker_id,
                MAX(score) as maxi_score
            FROM Submissions 
            GROUP BY hacker_id, challenge_id
        ) as cte
        GROUP BY hacker_id
        ) as  b
ON a.hacker_id = b.hacker_id
HAVING total_score > 0
ORDER BY total_score DESC, hacker_id
```