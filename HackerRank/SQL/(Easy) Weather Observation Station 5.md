[Weather Observation Station 5](https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

**MySql**

```sql
WITH cte AS (
  SELECT CITY, LENGTH(CITY) as len,
  ROW_NUMBER() OVER(ORDER BY LENGTH(CITY),CITY) as row_asc,
  ROW_NUMBER() OVER(ORDER BY LENGTH(CITY) DESC,CITY) as row_desc
  FROM STATION
ORDER BY LENGTH(CITY),CITY
)

SELECT CITY, len FROM cte
WHERE row_asc=1 or row_desc=1
```