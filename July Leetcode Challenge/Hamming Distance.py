class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=x^y
        hamming_dist=0
        while x>0:
            hamming_dist+=x&1
            x=x>>1
        return hamming_dist
