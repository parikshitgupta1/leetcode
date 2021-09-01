from typing import List, Set


class Solution:

    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        max_length = 0

        for i in nums:
            length = 0
            while not visited[i]:
                visited[i] = 1 
                length += 1     
                i = nums[i]    
            max_length = max(max_length, length)

        return max_length
