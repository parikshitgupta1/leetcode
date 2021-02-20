class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        last = None
        for d in s:
            if d == 'M':
                res += 800 if last == 'C' else 1000
            elif d == 'D':
                res += 300 if last == 'C' else 500
            elif d == 'C':
                res += 80 if last == 'X' else 100
            elif d == 'L':
                res += 30 if last == 'X' else 50
            elif d == 'X':
                res += 8 if last == 'I' else 10
            elif d == 'V':
                res += 3 if last == 'I' else 5
            else: # d == 'I'
                res += 1
            last = d
        return res
