[Top Competitors](https://www.hackerrank.com/challenges/full-score/problem)

**MySql**
```sql
SELECT s.hacker_id, h.name
FROM Challenges c JOIN Difficulty d JOIN Submissions s JOIN Hackers h

ON c.difficulty_level = d.difficulty_level
AND s.challenge_id = c.challenge_id
AND h.hacker_id = s.hacker_id
AND s.score = d.score

GROUP BY s.hacker_id, h.name
HAVING COUNT(s.challenge_id) > 1
ORDER BY COUNT(s.challenge_id) DESC, s.hacker_id
```

OR
```sql
select h.hacker_id, h.name from hackers h 
join submissions s using(hacker_id)
join challenges c using(challenge_id) 
join difficulty d using(difficulty_level)
where s.score=d.score 
group by h.hacker_id, h.name 
having count(s.challenge_id)>1 
order by count(s.challenge_id) desc, s.hacker_id
```