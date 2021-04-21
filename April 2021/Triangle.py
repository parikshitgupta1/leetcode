class Solution:
    def minimumTotal(self, triangle) -> int:
        triangle_memory = {}

        def dfs(t, r, c):
            if r == len(t):
                return 0
            if (r, c) in triangle_memory:
                return triangle_memory[(r, c)]
            
            triangle_memory[(r, c)] = t[r][c] + min(dfs(t, r+1, c), dfs(t, r+1, c+1))
            return triangle_memory[(r, c)]
        return dfs(triangle, 0, 0)

a = Solution()
print(a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
