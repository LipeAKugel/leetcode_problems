# O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            num_diff = target - nums[i]
            if (num_diff in nums_dict): 
                if (nums_dict[num_diff] != i):
                    return [i, nums_dict[num_diff]]


# O(n^2) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i, j]
