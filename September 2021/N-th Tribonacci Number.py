from typing import List

class Solution:
	def tribonacci(self, n: int) -> int:
		self.tribonacci_list: List = [0, 1, 1, 2]

		for i in range(4, n+1):
			self.tribonacci_list.append(sum(self.tribonacci_list[-3:]))

		return self.tribonacci_list[n]
