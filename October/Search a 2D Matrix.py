class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if len(matrix[i]) > 0 and target >= matrix[i][0] and target <= matrix[i][-1] and target in matrix[i]:
                return True
        return False
