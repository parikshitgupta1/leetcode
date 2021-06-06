class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         len_list = 0
         nums = set(nums)
         for x in nums:
                if x-1 not in nums:
                    y = x+1
                    while y in nums:
                        y+=1
                    len_list = max(len_list,y-x)
         return len_list
