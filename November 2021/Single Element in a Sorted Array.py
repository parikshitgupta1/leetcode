from typing import List
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i in range(len(nums)):
            if x[nums[i]]==1:
                return nums[i]
