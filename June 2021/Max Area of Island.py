class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
            
        max_area = 0
        visited = set([])
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue
                area = self.bfs(grid, x, y, visited)
                max_area = max(max_area, area)
                
        return max_area
        
    def bfs(self, grid, start_x, start_y, visited):
        queue = collections.deque([(start_x, start_y)])
        visited.add((start_x, start_y))
        area = 1
        
        while queue:
            x, y = queue.popleft()

            for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x, next_y = delta_x + x, delta_y + y
                
                if self.is_valid(grid, next_x, next_y, visited):
                   queue.append((next_x, next_y))
                   visited.add((next_x, next_y))
                   area += 1
            
            
        return area
        
    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False
            
        if y < 0 or y >= len(grid):
            return False
            
        if x < 0 or x >= len(grid[0]):
            return False
            
        if grid[y][x] == 0:
            return False
            
        return True
