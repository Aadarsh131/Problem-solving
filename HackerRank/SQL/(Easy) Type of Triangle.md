[Type of Triangle](https://www.hackerrank.com/challenges/what-type-of-triangle/problem)

**MySql**
> A Triangle has to satisfy-  
> 1. A+B > C 
> 2. B+C > A
> 3. C+A > B
```sql
SELECT 
    CASE
        WHEN A+B <= C OR B+C <= A OR C+A <= B THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A != B AND B != C AND A != C THEN 'Scalene'
        ELSE 'Isosceles'
    END
FROM TRIANGLES
```