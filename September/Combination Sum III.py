  
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []
        for c in combinations(nums, k):
            if n == sum(c):
                print(c)
                ans.append(list(c))

        return ans
