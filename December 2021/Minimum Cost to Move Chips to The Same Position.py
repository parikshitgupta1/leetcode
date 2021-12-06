from typing import List

class Solution:
	def minCostToMoveChips(self, positions: List[int]) -> int:
		even, odd = 0, 0
		for position in positions:
			if position % 2 == 0:
				even += 1
			else:
				odd += 1
		return min(even, odd)
