class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def updateMatrix(self, matrix):
        # write your code here
        n, m = len(matrix), len(matrix[0])
        dp = [[100000 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if (matrix[i][j] == 0):
                    dp[i][j] = 0
                if (i > 0):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if (j > 0):
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if (dp[i][j] > 0):
                    if (i < n - 1):
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if (j < m - 1):
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
