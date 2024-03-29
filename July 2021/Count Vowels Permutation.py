class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * 5 for _ in range(n)] 

        for j in range(5):
            dp[0][j] = 1

        for i in range(1, n):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod
            dp[i][3] = (dp[i-1][2]) % mod
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % mod

        return sum(dp[-1]) % mod
