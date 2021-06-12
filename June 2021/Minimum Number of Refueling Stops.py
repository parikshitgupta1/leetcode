from typing import List
from heapq import heappop, heappush


class Solution:
    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        stations = [[0, 0]] + stations + [[target, 0]]

        fuel = startFuel
        heap = []
        fuel_stops = 0

        for i in range(1, len(stations)):

            fuel -= stations[i][0] - stations[i-1][0]

            while heap and fuel < 0:
                fuel -= heappop(heap)
                fuel_stops += 1


            if fuel < 0:
                return -1

            heappush(heap, -stations[i][1])

        return fuel_stops
