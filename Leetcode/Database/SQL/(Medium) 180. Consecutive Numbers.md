[180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/description/)

**MySql**

1.  ```sql
    WITH cte AS (
    SELECT
        CASE 
            WHEN 
                LEAD(num, 1) OVER() = num -- since OVER() is compulsory with window func
                AND LEAD(id, 1) OVER() = id+1 -- id should also be sequential
                AND LEAD(num, 2) OVER() = num 
                AND LEAD(id, 2) OVER() = id+2
            THEN num 
        END AS ConsecutiveNums
    FROM logs
    )
    SELECT DISTINCT * FROM cte
    WHERE ConsecutiveNums IS NOT NULL;
    ```
    Outputs the `num` that appears **atleast 3 times consecutively**
    - `DISTINCT` can also be used on the outer query
        ```sql
        WITH cte AS (
            SELECT 
                DISTINCT --used here
                    CASE 
                        ...
                    END AS ConsecutiveNums
                FROM logs
        )
        SELECT * FROM cte --instead of here
        ...
        ```
2.  ```sql
    WITH cte AS (
        SELECT
            CASE 
                WHEN 
                    LEAD(num, 1) OVER() = num -- since OVER() is compulsory with window func
                    AND LEAD(id, 1) OVER() = id+1 -- id should also be sequential
                    AND LEAD(num, 2) OVER() = num
                    AND LEAD(id, 2) OVER() = id+2 
                THEN num 
            END AS ConsecutiveNums
        FROM logs
    )
    SELECT DISTINCT * FROM cte
    WHERE ConsecutiveNums IS NOT NULL;
    
    -- eg, the expected output is NULL here instead of 1, becuase we need the id's to be sequential as well
    -- | 1 | 1 |
    -- | 2 | 1 |
    -- | 4 | 1 |
    -- | 5 | 1 |
    -- | 6 | 2 |
    -- | 7 | 1 |
    ```
    - OR
        ```sql
        WITH cte AS (
            select 
                *,
                LEAD(num,1) OVER() AS num1,
                LEAD(id,1) OVER() AS id1, -- id should also be tracked for id sequence check
                LEAD(num,2) OVER() AS num2,
                LEAD(id,2) OVER() AS id2 
            FROM Logs
            )
        SELECT DISTINCT num AS ConsecutiveNums FROM cte WHERE (id1=id+1) AND (id2=id+2) AND (num1=num) AND (num2=num);
        ```
  