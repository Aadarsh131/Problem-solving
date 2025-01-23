[601. Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/description/)

# Intuition
1. First create all the `group of consecutives`
2. then, `GROUP BY` on it and output only the rows where its `COUNT()` >= 3

# Code
**MySql**
```sql
WITH grouped_consecutives AS(
    SELECT *,
        (@group := IF(id = @prev + 1, @group, @group + 1)) AS group_id,
        (@prev := id) AS prev_id
    FROM Stadium, (SELECT @prev := NULL, @group := 0) AS vars
    WHERE people >= 100
)

SELECT id, visit_date, people FROM grouped_consecutives WHERE group_id IN (
    SELECT group_id FROM grouped_consecutives GROUP BY group_id HAVING COUNT(id) >= 3
)
```
### Explanation

Lets say we have a column `num` with the values `1,2,3,5,6,9`
Grouping by the consecutives means just like this-
```makefile
id:      [1, 2, 3, 4, 5, 6]
num:     [1, 2, 3, 5, 6, 9]
Groups:  [1, 1, 1, 2, 2, 3]
``` 
We want to start making a new group whenever the sequence of the `id` is not correct
Lets create 2 variables, `@prev`(to keep track of row values) and `@group` (to keep track of groups)
```sql
(SELECT @prev := NULL, @group := 0) AS vars
```
then, check whether the current row's `id` is equal to `@prev` + 1 


```sql
@group := IF(id = @prev + 1, @group, @group + 1),
@prev := id AS prev_id
```
- if the `@prev + 1` *(last row's `id + 1`)* = `id` *(current row's `id`)* then, don't change the group, else increment the group value *(creating a new group)*  
- assign the current row's `id` to `@prev` to make it a previous value (`@prev`) for comparing it in the next row iteration

the logic is similar to (Optional)
```cpp
int group = 0;
int prev = -1;  // resembles the NULL in sql query
vector<int> num = {1, 2, 3, 5, 6, 9}; // 'num' table with values

for (int i = 0; i < num.size(); ++i) {
    int id = num[i]; // resembles automatically increment of the id

    if (id == prev + 1)
        group = group;// If id is consecutive, keep the same group
    else
        group++;// If not consecutive, increment the group

    prev = id;  // Update prev to the current id
}
```
**Output:**
|id|num	|@prev|	Condition (num = @prev + 1)|	@group Before|	New @group Assignment|
|---|---|---|---|---|---|
|1|1|	NULL|	FALSE *(NULL + 1 is invalid)*|	0|	1|
|2|2|	1|	TRUE|	1|	1|
|3|	3|	2|	TRUE|	1|	1|
|4|5|	3|	FALSE|	1|	2|
|5|6|	5|	TRUE|	2|	2|
|6|9|	6|	FALSE|	2|	3|

Now easily `GROUP BY` on `group_id` and count for rows `>=3`


<hr>

## A slightly different problem (a unique one)-
```sql
WITH grouped_consecutives AS(
    SELECT *,
        (@oldGroup:=@group),
        (@group := IF(id = @prev + 1, @group, @group + 1)) AS group_id,
        (@groupSum := IF(@group=@oldGroup, @groupSum + people, people)) as groupSum,
        (@prev := id) AS prev_id
    FROM Stadium, (SELECT @prev := NULL, @group := 0, @oldGroup:=0, @sum:=0) AS vars
    WHERE people >= 100
)

SELECT id, visit_date, people, group_id, groupSum FROM grouped_consecutives;
```
this will keep suming up the `people` for each `group`

Ouput:
```
+------+------------+--------+----------+----------+
| id   | visit_date | people | group_id | groupSum |
+------+------------+--------+----------+----------+
|    2 | 2017-01-02 |    109 | 1        |      109 |
|    3 | 2017-01-03 |    150 | 1        |      259 |
|    5 | 2017-01-05 |    145 | 2        |      145 |
|    6 | 2017-01-06 |   1455 | 2        |     1600 |
|    7 | 2017-01-07 |    199 | 2        |     1799 |
|    8 | 2017-01-09 |    188 | 2        |     1987 |
+------+------------+--------+----------+----------+
```