class Solution:
    def isIsomorphic(self, s, t):
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]] = t[i]
            elif map1[s[i]] != t[i]:
                return False
        for i in range(len(t)):
            if t[i] not in map2:
                map2[t[i]] = s[i]
            elif map2[t[i]] != s[i]:
                return False
        return True
