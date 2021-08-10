from functools import lru_cache


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, last):
            if i == n:
                return 0 
            d = ord(s[i]) - ord('0')
            dFlipped = 1 - d

            cand = []
            if dFlipped >= last:
                cand.append(dp(i + 1, dFlipped) + 1) 
            if d >= last:
                cand.append(dp(i + 1, d))  
            return min(cand)  

        return dp(0, 0)
