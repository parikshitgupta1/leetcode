class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        
        if not timeSeries: return 0
        
        total = 0
        next_ = timeSeries[0]+duration
        
        for i in range(1, len(timeSeries)):
            
            if timeSeries[i] >= next_:
                total += duration
            else:
                total += timeSeries[i] - timeSeries[i-1]
                
            next_ = timeSeries[i]+duration
            
        total += duration
        
        return total

print(Solution().findPoisonedDuration([1,2], 2))
