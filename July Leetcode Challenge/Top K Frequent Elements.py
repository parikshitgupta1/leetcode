class Solution:
    def topKFrequent(self, nums, k: int):
        numMap = Counter(nums)
        return sorted(numMap, key = numMap.get, reverse=True)[:k]
