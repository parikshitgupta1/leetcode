class Solution:
    def maxArea(self, height):
        max_area, beg, end = 0, 0, len(height) - 1
        while beg < end:
            max_area = max(max_area, min(height[beg], height[end]) * (end - beg))
            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1
        return max_area
