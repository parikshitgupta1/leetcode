import random
from bisect import bisect_right

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        areas = []
        for rect in rects:
            areas.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1))
        self.sum = [areas[0]]    
        for i in range(1, len(areas)):
            self.sum.append(self.sum[i-1] + areas[i])

    def pick(self) -> List[int]:
        rand = random.randint(0, self.sum[-1] - 1)
        index = bisect_right(self.sum, rand)
        rect = self.rects[index]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]
