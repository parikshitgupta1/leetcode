class Solution:
    def setZeroes(self, matrix):
        if len(matrix) == 0: return
        if len(matrix[0]) == 0: return 
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    self.mark(matrix, i, j) 
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 'N':
                    matrix[i][j] = 0
    
    def mark(self, matrix, i, j):
        for col in range(len(matrix[0])):
            if matrix[i][col] != 0:
                matrix[i][col] = 'N'
        for row in range(len(matrix)):
            if matrix[row][j] != 0:
                matrix[row][j] = 'N'
