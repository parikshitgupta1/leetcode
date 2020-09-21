class Solution:
	def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
		lst = []

		for n, start, end in trips:
			lst.append((start, n))
			lst.append((end, -n))
		lst.sort()

		passengers = 0
		for loc in lst:
			passengers += loc[1]
			if passengers > capacity:
				return False
		return True
