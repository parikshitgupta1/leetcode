class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        cnt = 0
        ending = 0
        for start,end in intervals:
            if ending < end:
                cnt+=1
                ending = end 
        return cnt
