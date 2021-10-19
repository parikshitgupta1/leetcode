class Solution:

    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        answer = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                answer[stack[-1]] = x
                del stack[-1]
            stack.append(x)
        for x in stack:
            answer[x] = -1
        return [answer[x] for x in nums1]
