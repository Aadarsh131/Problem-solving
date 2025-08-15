[Weather Observation Station 9](https://www.hackerrank.com/challenges/weather-observation-station-9/)

**MySql**
```sql
SELECT DISTINCT CITY FROM STATION
WHERE CITY NOT REGEXP '^[aeiou]'
```
- and `'.*[aeiou]$'` indicates *doesnot ends with vowels*
- `CITY NOT REGEXP '^[aeiou].*[aeiou]$'` indicates either doesnot starts with vowel or doesn't end with vowel