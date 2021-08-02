class Solution:
    def twoSum(self, numbers, target):
        for i, a in enumerate(numbers):
            for j, b in enumerate(numbers[i + 1 - len(numbers):]):
                if a + b == target:
                    return [i, j + i + 1]
        return [-1, -1]
