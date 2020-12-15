class Solution:
    def sortedSquares(self, nums):
        def squared(n):
            return n * n
        for i in range(0, len(nums)):
            nums[i] = squared(nums[i])
        return sorted(nums)
