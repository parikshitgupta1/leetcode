class Solution:
    def mincostTickets(self, days, cost):
        
        dp = [0 for _ in range(days[-1]+1)]
        dy = set(days)
        
        for i in range(days[-1]+1):
            if i not in dy:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-1)]+cost[0], dp[max(0,i-7)]+cost[1], dp[max(0,i-30)]+cost[2])
        return dp[-1]
