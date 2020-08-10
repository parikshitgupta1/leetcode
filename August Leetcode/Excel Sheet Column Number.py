class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
