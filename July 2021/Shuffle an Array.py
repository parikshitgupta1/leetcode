from random import shuffle
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.array = nums
        self.array_copy = nums.copy()

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        shuffle(self.array_copy)
        return self.array_copy
