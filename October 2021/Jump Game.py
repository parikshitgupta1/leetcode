class Solution(object):

    def canJump(self, nums):
        cur, last = 0, 0
        for i in nums:
            last, cur = max(last, cur + i), cur + 1
            if cur > last:
                break
        return True if cur == len(nums) else False
