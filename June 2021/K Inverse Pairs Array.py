class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        # As there is only one permutation with zero inverses, initialize 1
        dp = [[1] * (k+1) for _ in range(n+1)]
        # Also store cumulative sums
        sp = [[1] * (k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, k+1):
                # We can insert i in i different places and maintain inverse
                dp[i][j] = sp[i-1][j] if j < i else (sp[i-1][j] - sp[i-1][j-i])
                sp[i][j] = sp[i][j-1] + dp[i][j]

        return dp[-1][-1] % (10**9 + 7) 
