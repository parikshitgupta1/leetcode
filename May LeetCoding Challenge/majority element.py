from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_count=Counter(nums)
        number=list_count.most_common(1)[0][0]
        return number
