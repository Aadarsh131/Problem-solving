//https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<long long int> productExceptSelf(vector<long long int> &nums)
    {
        long long int product = 1;
        int zeroCount = 0;
        int len = nums.size();
        vector<long long int> res;
        for (int i = 0; i < len; i++)
        {
            if (nums[i] == 0)
            {
                zeroCount++;
                if (zeroCount >= 2)
                {
                    vector<long long int> res(len, 0);
                    return res;
                }
                continue;
            }
            product *= nums[i];
        }

        if (zeroCount == 1)
        {
            for (int i = 0; i < len; i++)
            {
                if (nums[i] == 0)
                    res.emplace_back(product);
                else
                    res.emplace_back(0);
            }
            return res;
        }
        // if no zeros in nums
        for (int i = 0; i < len; i++)
            res.emplace_back(product / nums[i]);
        return res;
    }

    void print(vector<long long int> &nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            cout << nums[i] << " ";
        }
    }
};

int main()
{
    Solution a;
    vector<long long int> nums = {4, 2, 2, 1, 2};
    vector<long long int> res = a.productExceptSelf(nums);
    a.print(res);
}