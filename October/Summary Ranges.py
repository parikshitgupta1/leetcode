class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        
        for i in nums:
            if i-1 not in nums:
                y = i + 1
                while y in nums:
                    y += 1
                if i == y - 1:
                    result.append(str(i))
                    
                else:
                    answer = str(i) + "->" + str(y-1)
                    result.append(answer)
        
        return result
