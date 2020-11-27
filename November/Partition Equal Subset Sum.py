class Solution:
    def canPartition(self, A):
        a = reduce(lambda a, num: a|(a<<num), A, 1)
        return sum(A)%2 == 0 and a & (1 << (sum(A)//2)) != 0
