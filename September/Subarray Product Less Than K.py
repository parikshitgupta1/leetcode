class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sub_array_product, left = 1, 0

        count = 0
        for right, right_num in enumerate(nums):
            sub_array_product = sub_array_product * right_num

            while sub_array_product >= k and left <= right:
                sub_array_product = sub_array_product // nums[left]
                left += 1

            if sub_array_product < k:
                length = right + 1 - left
                count += length
            else:
                pass

        return count
