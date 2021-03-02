from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        counter = Counter(nums)

        for x in counter:
            if counter[x] > 1:
                result.append(x)
        
        for i in range(1, len(nums) + 1, 1):
            if i not in counter:
                result.append(i)
                return result
