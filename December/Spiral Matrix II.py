class Solution:
    def generateMatrix(self, n: int):
        A, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(zip(*A[::-1]))
        return A
