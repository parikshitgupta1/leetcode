from itertools import combinations
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
        nums.sort()  
        for length in range(len(nums)+1):
            combo = set(combinations(nums, length)) 
            subsets += list(map(list, combo))  
        return subsets
