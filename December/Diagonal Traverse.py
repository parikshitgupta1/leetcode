class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        levels = defaultdict(list)
        for i, j in product(range(m), range(n)):
            levels[i+j].append(matrix[i][j])
                
        out = []
        for lev in range(m + n):
            out += levels[lev][::lev%2*2-1]   
        return out
