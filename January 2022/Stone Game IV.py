class Solution:
	def winnerSquareGame(self, n: int) -> bool:
		dp = [0] * (n+1)
		for i in range(1, n+1):
			j = 1
			while j * j <= i and not dp[i]:
				dp[i] = dp[i-j*j]^1
				j += 1
		return dp[n]
