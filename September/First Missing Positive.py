class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 1

		if nums:
			max_value = max(nums)
		else:
			max_value = 1

		if max_value < 0:
			return 1

		for i in range(1, max_value+2):
			if i not in nums:
				return i
