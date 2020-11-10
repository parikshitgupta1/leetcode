class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        reversed_A = []
        for i in A:
            reversed_A.append(i[::-1])
        for i in range(len(reversed_A)):
            for j in range(len(A[i])):
                if reversed_A[i][j] == 1:
                    reversed_A[i][j] = 0
                else:
                    reversed_A[i][j] = 1
        return reversed_A
