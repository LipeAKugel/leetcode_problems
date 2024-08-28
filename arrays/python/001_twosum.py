class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    num_dict = {}
    
    for i in range(0, n):
      if (target - nums[i]) in num_dict.keys():
        return [num_dict[target - nums[i]], i]
      num_dict[nums[i]] = i
    
    return [-1, -1]
