class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root)-> List[int]:
        result = []

        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                stack.extend(root.children[::-1])
        return result
