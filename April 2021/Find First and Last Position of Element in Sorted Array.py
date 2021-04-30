class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        i = nums.index(target)
        j = i
        for x in range(i+1, len(nums)):
            if nums[x]!=target:
                break
            j = x
        return [i, j]


a = Solution()
print(a.searchRange([5,7,7,8,8,10], 8))
