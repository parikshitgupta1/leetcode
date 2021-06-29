class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = int()
        start_ptr = int()
        n_zeroes = int()

        for end_ptr in range(len(nums)):
            if nums[end_ptr] == 0:
                n_zeroes += 1

            while n_zeroes > k:
                if nums[start_ptr] == 0:
                    n_zeroes -= 1
                start_ptr += 1
            max_length = max(max_length, end_ptr-start_ptr+1)

        return max_length
