class Solution:
    def numPairsDivisibleBy60(self, time):
        res, count = 0, [0] * 60
        for one in range(len(time)):
            index = time[one] % 60
            res += count[(60 - index) % 60]  # %60 is for index==0
            count[index] += 1
        return res
