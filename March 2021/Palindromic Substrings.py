class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        def getPCount(b, e):
            ans = 0
            while b>=0 and e<length and s[b] == s[e]:
                b-=1
                e+=1
                ans+=1
            return ans
        
        ret = 0
        for i in range(length):
            ret+=getPCount(i, i)
            if i>0:
                ret+=getPCount(i-1, i)
        
        return ret
