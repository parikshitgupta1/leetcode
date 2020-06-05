class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        s = 0
        for weight in w:
            s += weight
            self.prefix_sum.append(s)
        self.total = s

    def pickIndex(self) -> int:
        random_num = self.total * random.random()
        low, high = 0, len(self.prefix_sum)
        while(low < high):
            mid = low + (high - low) // 2
            if(random_num > self.prefix_sum[mid]):
                low = mid + 1
            else:
                high = mid
        return low
