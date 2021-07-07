from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        req = n // 2

        frequency = Counter(arr).most_common()
        result = 0

        while n > req:
            n -= frequency.pop(0)[1] 
            result += 1

        return result
