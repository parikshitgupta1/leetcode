class Solution:
    def maxProfit(self, B, fee):
        if len(B) == 1: return 0
        n = len(B)
        
        dp, sp = [-float(inf)]*n, [0]*n

        for i in range(n-1):
            dp[i] = B[i+1] - B[i] + max(dp[i-1], sp[i-2] - fee)
            sp[i] = max(sp[i-1], dp[i])
             
        return sp[-2] 
