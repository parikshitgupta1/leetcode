class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sortints = sorted([(inter, i) for i, inter in enumerate(intervals)]) + [([max(intervals, key=lambda x: x[1])[1] + 1, 0],-1)]
        begs = [inter[0][0] for inter in sortints]
        res = [0] * len(intervals)
        for inter in sortints[:-1]:
            res[inter[1]] = sortints[bisect.bisect_left(begs, inter[0][1])][1]
        return res
