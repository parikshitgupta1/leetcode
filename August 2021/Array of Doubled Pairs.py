from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = Counter(arr)  
        arr.sort(key=abs)    

        for num in arr:
            if freq[num] == 0:
                continue     
            if freq[2*num] == 0:
                return False 
            freq[num] -= 1
            freq[2*num] -= 1

        return True 
