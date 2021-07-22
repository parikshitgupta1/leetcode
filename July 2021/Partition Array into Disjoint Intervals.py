from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = all_max = nums[0]
        ptr_index = 0  
        for i in range(len(nums)):
            all_max = max(all_max, nums[i])
            if nums[i] < left_max:
                ptr_index = i
                left_max = all_max
        return ptr_index + 1 
