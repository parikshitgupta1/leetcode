class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        n = len(nums)
        s = set(nums)
        res = [i for i in range(1, n+1) if i not in s]
        return res
