from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if k - node.val in visited:
                return True
            visited.add(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
