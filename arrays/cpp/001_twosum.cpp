#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {  
    unordered_map<int, int> ump;
    int n = nums.size();

    for(int i = 0; i < n; i++) {
      if (ump.find(target-nums[i]) != ump.end()) {
        return vector<int> ({ump[target-nums[i]], i});
      }
      ump[nums[i]] = i;
    }

    return vector<int> ({-1, -1});
  }
};