class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = list()

        for node in preorder:
            while stack and node == "#" and stack[-1] == "#":
                stack.pop()
                if not stack:
                    return False
                stack.pop()
                print(stack)
            stack.append(node)
        return stack == ["#"]
