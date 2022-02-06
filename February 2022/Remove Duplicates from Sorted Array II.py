class Solution:
    def removeDuplicates(self, nums):
        for num in nums[::-1]:
            if nums.count(num) > 2:
                nums.remove(num)
        return len(nums)
