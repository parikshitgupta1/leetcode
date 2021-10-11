"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def _diameterOfBinaryTree(root: TreeNode) -> int:
            if root is None:
                return 0, 0

            l, lbelow = _diameterOfBinaryTree(root.left)
            r, rbelow = _diameterOfBinaryTree(root.right)

            return max(l + 1, r + 1) , max(l + 1 + r, lbelow, rbelow)

        return max(max(_diameterOfBinaryTree(root)) - 1, 0)
