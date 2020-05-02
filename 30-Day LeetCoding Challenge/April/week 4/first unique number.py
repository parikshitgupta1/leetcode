from collections import defaultdict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniques = []
        self.counts = defaultdict()
        for x in nums:
            self.add(x)
        
    def showFirstUnique(self) -> int:
        while len(self.uniques) > 0 and self.counts[self.uniques[0]] > 1:
            self.uniques.pop(0)
        if len(self.uniques) > 0:
            return self.uniques[0]
        else:
            return -1
                    
    def add(self, value: int) -> None:
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1
            self.uniques.append(value)
