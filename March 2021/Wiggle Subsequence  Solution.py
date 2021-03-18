class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        print(diffs)
        run1 = 1
        sign = 1
        for diff in diffs:
            if diff < 0 and sign == 1:
                sign = -1
                run1 += 1
            elif diff > 0 and sign == -1:
                sign = 1
                run1 += 1
        
        run2 = 1
        sign = -1
        for diff in diffs:
            if diff < 0 and sign == 1:
                sign = -1
                run2 += 1
            elif diff > 0 and sign == -1:
                sign = 1
                run2 += 1
        return max(run1, run2)
