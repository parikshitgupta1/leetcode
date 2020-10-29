class Solution:
	def maxDistToClosest(self, seats: List[int]) -> int:
		distances = [float("inf")] * len(seats)
		max_distance = 0
		index = -1

		for i in range(len(seats)):
			if seats[i] == 0:
				if index == -1:
					continue
				distances[i] = i - index
			else:
				index = i

		index = -1
		for i in range(len(seats) - 1, -1, -1):
			if seats[i] == 0:
				if index == -1:
					continue
				distances[i] = min(distances[i], index - i)
			else:
				index = i

		for distance in distances:
			if distance != float("inf"):
				max_distance = max(max_distance, distance)

		return max_distance
