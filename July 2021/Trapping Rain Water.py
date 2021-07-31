from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Edge case
        if n <= 2:
            return 0 

        left_max = height[0]
        left_high = [left_max]  
        for i in range(1, n):
            if height[i] > left_max:
                left_max = height[i]
            left_high.append(left_max)

        right_max = height[n-1]
        right_high = [right_max]  
        for i in range(n-2, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            right_high.insert(0, right_max)

        ans = 0
        for i in range(n):
            ans += (min(left_high[i], right_high[i]) - height[i])
        return ans
