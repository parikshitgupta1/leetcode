class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()

        for ch in s:
            stack.append(ch)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

        return ''.join(stack)
