class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res=0
        self.directions=[(1,0),(-1,0),(0,1),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res+=1               
                    self.dfs(grid,i,j)
        return res
    def dfs(self,grid,i,j):
        if grid[i][j]!='1':
            return 
        grid[i][j]='*'
        for p,q in self.directions:
            x=i+p
            y=j+q
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                self.dfs(grid,x,y)   
