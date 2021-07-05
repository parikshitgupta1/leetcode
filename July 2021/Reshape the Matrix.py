from typing import List

class Solution:

    def matrixReshape(self, mat: List[List[int]],
                      r: int, c: int) -> List[List[int]]:
        m = len(mat) 
        n = len(mat[0]) 

        if m*n != r*c:
            return mat

        elements = [element for row in mat for element in row] 
        new_matrix = list()

        for row in range(r):
            new_matrix.append(elements[row*c : (row+1)*c])

        return new_matrix
