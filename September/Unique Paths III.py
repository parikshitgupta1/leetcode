class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.steps = 0
        self.result = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    self.steps += 1
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    self.dfs(row + 1, col)
                    self.dfs(row - 1, col)
                    self.dfs(row, col + 1)
                    self.dfs(row, col - 1)
        return self.result

    def dfs(self, row, col, steps_count = 0):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] == -1:
            return
        elif self.grid[row][col] == 2 and steps_count == self.steps:
            self.result += 1
        elif self.grid[row][col] == 0:
            self.grid[row][col] = -1
            self.dfs(row + 1, col, steps_count + 1)
            self.dfs(row - 1, col, steps_count + 1)
            self.dfs(row, col + 1, steps_count + 1)
            self.dfs(row, col - 1, steps_count + 1)
            self.grid[row][col] = 0
