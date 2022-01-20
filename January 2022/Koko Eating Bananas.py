import math

class Solution:
    def minEatingSpeed(self, piles, H):
        if len(piles) > H:
            return -1
        
        small_k = 1
        large_k = max(piles)
        while small_k + 1 < large_k:
            mid_k = small_k + (large_k - small_k) // 2
            if self.can_finish(piles, H, mid_k):
                large_k = mid_k
            else:
                small_k = mid_k
        if self.can_finish(piles, H, small_k):
            return small_k
        else:
            return large_k
    
    def can_finish(self, piles, H, K):
        hours = 0
        for p in piles:
            hours += math.ceil(p / K)
        return hours <= H
