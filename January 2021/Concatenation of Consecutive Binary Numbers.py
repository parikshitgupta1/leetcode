class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = (10 ** 9) + 7
        concate = ""
        for i in range(1, n + 1):
            temp = bin(i)
            concate += temp[2:]

        new = int(concate, 2)
        return new % mod
