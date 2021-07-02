from typing import List
from collections import deque


class Solution:
    def findClosestElementsUsingDeque(self, arr: List[int], k: int, x: int) -> List[int]:
        new = deque(arr)
        while len(new) > k:
            new.pop() if abs(new[0]-x) <= abs(new[-1]-x) else new.popleft()
        return list(new)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while(left < right):
            mid = (left + right) // 2
            if(x - arr[mid]) > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
