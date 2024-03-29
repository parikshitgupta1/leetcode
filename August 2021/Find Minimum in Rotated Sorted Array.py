from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[-1]:
                left = mid + 1  
            elif nums[mid] < nums[-1]:
                right = mid - 1  

        return 
