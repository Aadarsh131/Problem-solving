**TAGS**- `array` `hashtable`  
**Problem**- https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/   

**Approach/Intuition no. [1](#approach-1), [2](#approach-2) (optimal solution, without hashmap)**   

<h4 id = "approach-1"> <u>Approach 1</u>-</h4>

Keep track of what position is the new occurence of `x` happened using an unordered_map i.e, a map of (`occurence of x -> pos`)  

Now scan through the queries array and find if the `queries[i]th` element(i.e, `occurence of x`) is present in map and push the value (i.e, `pos`) in a new `res` array, if it is present else push `-1`

Return the `res` array

```cpp
class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
       int occCount=0; //count of the occurence

       //using ordered map
       map<int, int> OccAndPos; //occ of x, pos
       for(int i=0;i<nums.size();i++){
        if(nums[i] == x){
            occCount++;
            OccAndPos[occCount] = i;
        }
       }

        vector<int> res;
       //check hashmap with queries array
       for(int i=0;i<queries.size();i++){

        //if queries[i]th occurence is found in nums (which we are confirming it with our custom hashmap)
        if(OccAndPos.find(queries[i]) != OccAndPos.end())
            res.push_back(OccAndPos[queries[i]]);
        else
            res.push_back(-1);
       }
       return res;
    }
};
```

<h4 id = "approach-2"> <u>Approach 2</u>-</h4>

Keep track of what position is the new occurence of x happened, this time in an array `pos` (eg, `[0,3,5]`- 1st occurence of x is found at pos/index 0, 2nd occurence at pos/index 3 and 3rd occurence at pos/index 5)

Maximum occurence of `x` should now be `len(pos)`, with this in mind make a new vector `res` array of size of `queries`, and make all the index of `res` array to be equal to `-1` of size `len(queries)`.

Now if `queries[i] > len(pos)` (meaning, `queries[i]th` occurence of `x` is not present), then leave the indexto be `-1` and make the rest of index of `res` array (i.e, when `queries[i] <= len(pos)`) equal to `pos[queries[i]-1]`

Return the `res` array

```cpp
class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
      vector<int> pos; //positions of occurences of x
      for(int i=0; i<nums.size(); i++){
        if (nums[i] == x){
            pos.push_back(i);
        }
      }
    
      int lenQueries = queries.size(); //length of queries
      int lenPos = pos.size(); //lenght of Pos
      vector<int> res(lenQueries, -1);
      for(int i = 0; i< lenQueries; i++){
        if (queries[i] <= lenPos){
            res[i] = pos[queries[i]-1];
        }
      }
      return res;
    }
};
```