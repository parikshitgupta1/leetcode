class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j]==arr[i]+1:
                    count += 1
                    break
        
        return count      
