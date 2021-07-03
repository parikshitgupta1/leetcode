from bisect import bisect_left, insort
from itertools import accumulate, product, combinations
from math import inf
from typing import List

class Solution:

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix) 
        N = len(matrix[0])  
        ans = -inf

        def countRangeSum(nums, upper):
            sorted_list = [0]
            ans = -inf
            for s in accumulate(nums):  
                index = bisect_left(sorted_list, s - upper)
                if index < len(sorted_list):
                    ans = max(ans, s - sorted_list[index])
                insort(sorted_list, s)
            return ans


        for i, j in product(range(1, M), range(N)):
            matrix[i][j] += matrix[i-1][j]  
        matrix = [[0]*N] + matrix  

        for row1, row2 in combinations(range(M+1), 2):
            row = [j-i for i, j in zip(matrix[row1], matrix[row2])]
            ans = max(ans, countRangeSum(row, k))

        return ans
