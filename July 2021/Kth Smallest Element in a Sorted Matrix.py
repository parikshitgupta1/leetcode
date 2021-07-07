from bisect import bisect
from typing import List

class Solution:
    def count(self, matrix: List[List[int]], num: int) -> int:
        count = 0
        for row in matrix:
            count += bisect(row, num)
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]  
        right = matrix[-1][-1]

        while left <= right:
            mid = (left + right) // 2
            if self.count(matrix, mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left
