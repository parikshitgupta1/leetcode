from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = sorted(s, reverse = True)
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        count = 0
        flag = 0
        for key, value in d.items():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                flag += 1
        if flag:
            return count + 1
        return count
