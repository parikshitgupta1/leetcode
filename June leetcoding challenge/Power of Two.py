class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1 and not n & 1:
            n >>= 1
        return n == 1
