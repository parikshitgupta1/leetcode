class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        idx = 1
        while n > 0:
            n -= idx
            if n >= 0:
                rows += 1
            idx += 1
        return rows
