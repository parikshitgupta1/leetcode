class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s == "") or (len(set(list(s))) == 1):
            return s
        m = s[0]
        for i in range(len(s)):
            if len(s) - i < len(m):
                break
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if (j - i) > len(m):
                        m = s[i:j]
                        break

        return m
