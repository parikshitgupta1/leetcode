class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for c in s:
            lo, hi = lo+1 if c == '(' else max(0, lo-1), hi-1 if c == ')' else hi+1
            if hi < lo:
                return False
        return lo <= 0 <= hi
