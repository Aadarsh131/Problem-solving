[Challenges](https://www.hackerrank.com/challenges/challenges/problem)

**MySql**
```sql
WITH cte AS(
    SELECT hacker_id, COUNT(challenge_id) as challenges_created     FROM Challenges 
    GROUP BY hacker_id
    ORDER BY challenges_created DESC
), max_chal AS(
    SELECT MAX(challenges_created) as challenges_created FROM cte
)

SELECT cte.hacker_id, name, challenges_created FROM cte JOIN Hackers ON cte.hacker_id = Hackers.hacker_id
WHERE challenges_created IN (
    SELECT 
        CASE 
            WHEN LAG(challenges_created,1) OVER() =challenges_created OR LEAD(challenges_created,1) OVER() =challenges_created THEN NULL
            ELSE challenges_created
        END
    FROM cte WHERE challenges_created NOT IN (SELECT * FROM max_chal)
    )
    
    OR
    challenges_created IN (SELECT * FROM max_chal)


ORDER BY challenges_created DESC, cte.hacker_id
```