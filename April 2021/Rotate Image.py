class Solution:
    def rotate(self, matrix) -> None:
        result = []
        for i in range(0,len(matrix)):
            store = []
            for j in range(len(matrix)-1,-1,-1):
                store.append(matrix[j][i])
    
            result.append(store)
        for i in range(0,len(result)):
            matrix[i] = result[i]
        return matrix


a = Solution()
print(a.rotate([[1,2],[3,4]]))
