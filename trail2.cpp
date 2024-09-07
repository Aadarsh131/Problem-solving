#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int maxArea(vector<int> &height)
{
  int len = height.size();
  int maxi = 0;

  int i = 0;
  int j = len - 1;
  while (i < j)
  {
    int lowestHeight = min(height[i], height[j]);
    int area = lowestHeight * (j - i);
    if (area > maxi)
      maxi = area;

    int temp_i = i + 1;
    while (height.at(temp_i) <= height[i] && temp_i < j)
    {
      temp_i++;
    }
    i = temp_i;

    lowestHeight = min(height[i], height[j]);
    area = lowestHeight * (j - i);
    if (area > maxi)
      maxi = area;

    int temp_j = j - 1;
    while (height.at(temp_j) <= height[j] && i < temp_j)
    {
      temp_j--;
    }
    j = temp_j;
  }
  return maxi;
}

int main()
{
  // vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
  vector<int> height = {1,2,3,4,5,6,7};
  cout << maxArea(height) << endl;
}
