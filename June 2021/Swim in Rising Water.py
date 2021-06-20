from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)  # NxN grid
        minDepth = 0
        maxDepth = N**2 - 1  # According to constraints

        def dfs(x: int, y: int) -> None:
            if not visited[x][y] and grid[x][y] <= midDepth:
                # We can access grid at current depth t
                visited[x][y] = True
                if x-1 >= 0:
                    dfs(x-1, y)  # Move left
                if x+1 < N:
                    dfs(x+1, y)  # Move right
                if y-1 >= 0:
                    dfs(x, y-1)  # Move top
                if y+1 < N:
                    dfs(x, y+1)  # Move bottom

        while minDepth < maxDepth:
            midDepth = (minDepth + maxDepth) // 2
            visited = [[False]*N for _ in range(N)]
            dfs(0, 0)  # Start from first grid square with minDepth
            if visited[-1][-1]:
                # We can reach the last grid square
                maxDepth = midDepth
            else:
                # We cannot reach the last grid square with current depth
                minDepth = midDepth + 1

        return minDepth
