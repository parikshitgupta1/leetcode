class Solution:
    def largestIsland(self, grid):
        N = len(grid)
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j
        def dfs(x, y, index):
            area = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    area += dfs(i, j, index)
            return area + 1
        index = 2
        area = {}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1
        res = max(area.values() or [0])
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y) if grid[i][j] > 1)
                    res = max(res, sum(area[index] for index in possible) + 1)
        return res
