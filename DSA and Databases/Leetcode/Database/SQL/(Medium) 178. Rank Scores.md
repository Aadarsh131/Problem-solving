[178. Rank Scores](https://leetcode.com/problems/rank-scores/description/)

**MySql** (bruteforce)
```sql
With distinct_score AS (
    SELECT DISTINCT score FROM Scores ORDER BY score DESC
),
distinct_rank AS (
    SELECT score, RANK() OVER(ORDER BY score DESC) as `rank` FROM distinct_score
)

SELECT s.score, `rank` FROM Scores s JOIN distinct_rank d ON s.score=d.score ORDER BY `rank` 
```
- **Intuition**: find the `distinct` score with their ranks, then filter out only those rows from `Scores` table where `(score,rank)` rows from the `distinct_rank` table applies
- NOTE- **\` rank \`** is used with backticks as var `rank` is a reserved keyword in Mysql

**MySql** (Optimal sol, using built in `DENSE_RANK()` window fn)
```sql
Select score,
       DENSE_RANK() Over (Order By score Desc) `rank`
From Scores
```