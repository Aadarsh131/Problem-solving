[Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/)

**MySql**

```sql
SELECT Distinct CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$'
```
- `^` asserts the start of string
- `$` asserts the end of string
- `.*` maches any sequence of char in the middle 