class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :param m: {int} number of columns
        :param n: {int} number of rows
        :return: {int} number of unique path to reach to block [n-1][m-1] from block [0][0]
        """
        # build (m*n) grid of 1's
        grid = [[0 for _ in range(m)] for _ in range(n)]

        row, col = n - 1, m - 1

        # start traversing from bottom point
        for i in range(row, -1, -1):
            for j in range(col, -1, -1):
                if i == row or j == col:
                    grid[i][j] = 1
                else:
                    grid[i][j] += grid[i][j + 1] + grid[i + 1][j]

        return grid[0][0]
