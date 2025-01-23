[Weather Observation Station 20](https://www.hackerrank.com/challenges/weather-observation-station-20)

**MySql**
```sql
SELECT ROUND(LAT_N,4) FROM 
(SELECT LAT_N, ROW_NUMBER() OVER(ORDER BY LAT_N) as rn FROM STATION) as subquery
WHERE rn = (
    SELECT IF(COUNT(*) % 2 = 0, COUNT(*)/2, (COUNT(*)+1)/2) 
    FROM STATION
)
```