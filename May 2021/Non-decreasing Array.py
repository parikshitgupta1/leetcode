class Solution(object):
    def checkPossibility(self, nums):
        modified, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                if modified:
                    return False
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    prev = nums[i]    
                modified = True
            else:
                prev = nums[i]
        return True
