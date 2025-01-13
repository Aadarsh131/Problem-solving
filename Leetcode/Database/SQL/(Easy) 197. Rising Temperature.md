[197. Rising Temperature](https://leetcode.com/problems/rising-temperature/description/)

# Intuition and Approach

> It first sorts the table taking `O(n)` time, then compares each row using `lag()` taking `0(n)` time.
> So, in total `O(n+n) = O(2n) ~ O(n)` time complexity

1. First sort by `recordDate`
    ```sql
    order by recordDate
    ```
2. then apply window function `lag()` to check for previous row's/yesterday's value
3. then compare those values with your *desired values*
    ```sql
    when 
        --comparing with previous day's temperature with current day
        ((lag(temperature,1) over() < temperature) 

    and -- outputs true if both the operands are true

        -- checking only for the yesterday's date
        lag(recordDate,1) over() = date_sub(recordDate, interval 1 day)) 
    ```
    - `lag(temperature, 1) over()` and `lag(recordDate, 1) over()`will check for its previous row
        > **NOTE:** `over()` is still required as per the syntax, even if we are not providing any `partition by` or `order by` clause in it
    
    - `date_sub(recordDate, interval 1 day)` meaning substract `1 day` from the current `recordDate`
    
        > **NOTE**: don't use `date = date - 1` approach
        >   - *Reason*- as `('2020-05-01') - 1` = `'2020-05-00'` *(which is wrong)*
        >   - *Solution*- use `date_sub()`, so now `date_sub(('2020-05-01') interval 1 day`= `2020-04-30`  *(which is correct)*

4. we will be filtering out the `null` values that might have come from the cases above when the condition doesn't hold `true`
    eg. 
    1. when previous row's date is not yesterday's date
    2. when previous row's/date's temperature is not less than today's row/date
    ```sql
    where id is not null
    ```

### Full Code 
**MySql**
```sql
select id from (
    select 
        CASE when 
            ((lag(temperature,1) over() < temperature)
            and
            lag(recordDate,1) over() = date_sub(recordDate, interval 1 day))
            then id 
        END as id
    from Weather
    order by recordDate
    ) as subquery
where id is not null
```
 