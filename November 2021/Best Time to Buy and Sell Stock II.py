class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        dp = [0] * 3
        max_diff = float("-inf")

        for i in range(2, len(prices) + 1):
            max_diff = max(max_diff, dp[(i + 1) % 3] - prices[i - 2])
            dp[i % 3] = max(dp[(i + 2) % 3], max_diff + prices[i - 1])

        return max(dp)
