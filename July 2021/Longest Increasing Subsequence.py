from bisect import bisect_left
from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = list()  

        for num in nums:
            index = bisect_left(sub, num) 
            if index == len(sub):
                sub.append(num)  
            else:
                sub[index] = num 

        return len(sub)
