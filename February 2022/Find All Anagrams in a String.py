from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def Counter(a):
            d = {}
            for c in a:
                d[c] = d.get(c,0) + 1
            return d
        
        ans = []
        pl = len(p)
        dp  = Counter(p)
        ds  = Counter(s[:pl-1])

        for i in range(pl-1,len(s)):
            
            ds[s[i]] = ds.get(s[i],0) + 1
            
            if ds == dp:
                ans.append(i-pl+1)

            ds[s[i-pl+1]] =  ds.get(s[i-pl+1],1) - 1
            if ds[s[i-pl+1]] == 0:
                del ds[s[i-pl+1]]
                
        return ans
