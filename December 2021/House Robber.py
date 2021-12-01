class Solution:
    def rob(self, nums):
        
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1+num, dp2)
            
        return dp2

print(Solution().rob([2,7,9,3,1]))
