from collections import defaultdict
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        rank = [0] * (rows + cols)

        indices = defaultdict(list) 
        for row in range(rows):
            for col in range(cols):
                indices[matrix[row][col]].append([row, col])

        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        for val in sorted(indices):
            parent = list(range(rows + cols))
            rank2 = rank.copy()
            for row, col in indices[val]:
                row, col = find(row), find(rows + col)
                parent[row] = col
                rank2[col] = max(rank2[row], rank2[col])
            for row, col in indices[val]:
                rank[row] = rank[rows + col] = \
                    matrix[row][col] = rank2[find(row)] + 1

        return matrix
