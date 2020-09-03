class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = s + s
        if s in double_s[1:-1]:
            return True
        return False
