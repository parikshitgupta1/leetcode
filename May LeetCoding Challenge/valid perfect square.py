class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        s, i = 0, 1
        while s < num:
            s = s + i
            i += 2
        if s == num:
            return True
        return False
