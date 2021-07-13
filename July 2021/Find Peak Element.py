from math import inf
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1

        left = 0
        right = n-1

        while left <= right:
            mid = left + (right - left) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) \
                    and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif (mid > 0 and nums[mid-1] > nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
