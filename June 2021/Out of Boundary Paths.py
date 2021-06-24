class Solution:

    def findPaths(self, m: int, n: int, maxMove: int,
                  startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            a = solve(i-1, j, maxMove-1)  # Left
            b = solve(i+1, j, maxMove-1)  # Right
            c = solve(i, j-1, maxMove-1)  # Top
            d = solve(i, j+1, maxMove-1)  # Bottom

            return a + b + c + d

        return solve(startRow, startColumn, maxMove) % (10**9 + 7)
