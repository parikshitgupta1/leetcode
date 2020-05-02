class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Initialize first row and col
        for j in range(1, num_cols):
            grid[0][j] += grid[0][j-1]
        for i in range(1, num_rows):
            grid[i][0] += grid[i-1][0]

        # Fill in DP grid
        for j in range(1, num_cols):
            for i in range(1, num_rows):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

if __name__ == '__main__':
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    ans = Solution().minPathSum(grid)
    print(ans)
        
