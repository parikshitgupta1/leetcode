from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            self._sums = [0]
            return
        elif len(nums) == 1:
            self._sums = [nums[0]]
        else:
            self._sums = [nums[0]]
            for i in range(1, len(nums)):
                self._sums.append(self._sums[i - 1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self._sums[j]
        
        return self._sums[j] - self._sums[i - 1]
