class Solution:
    def numberOfArithmeticSlices(self, A):
        B =  [j-i for i,j in zip(A, A[1:])]
        return sum(((2*len(list(j))-1)**2-1)//8 for i, j in groupby(B))
