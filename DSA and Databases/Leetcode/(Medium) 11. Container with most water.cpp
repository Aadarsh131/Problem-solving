#include <iostream>
#include <vector>
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

    if (height[i] < height[j])
      i++;
    else
      j--;
  }
  return maxi;
}

int main()
{
  vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
  cout << maxArea(height) << endl;
}