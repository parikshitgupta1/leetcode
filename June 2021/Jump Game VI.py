class Solution:
    '''
    Time Complexity: O(n)
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([0])  # Maintain indices, not numbers themselves

        for i in range(1, len(nums)):
            while dq and dq[0] < i-k:
                dq.popleft()  # Remove elements outside the k element window
            nums[i] += nums[dq[0]]  # First element of deque is max index
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()  # To make space for new element and maintain order
            dq.append(i)

        return nums[-1]
