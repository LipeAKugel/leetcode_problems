from typing import List

# Solution using dictionaries.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num in hash:
                return True
            hash[num] = num

        return False

# Solution using sets.
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for num in nums:
            if num in numset:
                return True
            numset.add(num)

        return False
