class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
    
            if nums[i]==target:
                return i
                
            if nums[i]>target:
                return i
                 
        return i+1
