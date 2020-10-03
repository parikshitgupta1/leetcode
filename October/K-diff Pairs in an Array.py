class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        cnt = 0
        for n in nums:
            d[n] = d.get(n,0)+1 
        
        for n in d:
            if k == 0:
                if d[n] > 1: cnt+=1 
            else:
                if n+k in d:
                    cnt+=1 
        return cnt
