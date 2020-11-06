import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        values = range(1, nums[-1] + 1)
        l, r = 0, len(values) - 1
        sdgt = float('inf')

        while(r >= l):
            mid = l + (r - l) // 2
            tot = 0
            for num in nums:
                tot += math.ceil(num/values[mid])
            # print("l: " + str(l) + ", r: " + str(r) + ", mid: " + str(mid) + ", tot: " + str(tot))
            if tot > threshold:
                l = mid + 1
            else:
                sdgt = min(values[mid], sdgt)
                r = mid - 1
        return sdgt
