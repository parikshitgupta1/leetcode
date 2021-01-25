class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dist = k

        for num in nums:
            if num == 0:
                dist += 1
            elif num == 1 and dist >= k:
                dist = 0
            else:
                return False

        return True
