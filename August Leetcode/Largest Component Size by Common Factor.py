import math

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factors = {}
        numbers = list(range(max(A)+1))
        for number in A:
            for factor in range(2, int(math.sqrt(number))+1):
                if not number % factor:
                    self.union(numbers, number, factor)
                    self.union(numbers, number, number // factor)
        for number in A:
            number = self.unionFind(numbers, number)
            if number not in factors:
                factors[number] = 0
            factors[number] += 1
        return max(factors.values())

    def unionFind(self, numbers, number):
        while numbers[number] != number:
            numbers[number] = numbers[numbers[number]]
            number = numbers[number]
        return number

    def union(self, numbers, number, factor):
        if numbers[number] == numbers[factor]:
            return
        new_number = self.unionFind(numbers, number)
        new_factor = self.unionFind(numbers, factor)
        numbers[new_number] = new_factor
