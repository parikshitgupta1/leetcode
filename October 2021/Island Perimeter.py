class Solution:
    def islandPerimeter(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        p = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                p += self.isLand(grid, i + 1, j) + self.isLand(grid, i - 1, j) + \
                     self.isLand(grid, i, j + 1) + self.isLand(grid, i, j - 1)
        return p

    def isLand(self, grid, i, j):
        try:
            if i < 0 or j < 0:
                return 1
            return not grid[i][j]
        except:
            return 1
