from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_sum(self, node: TreeNode) -> int:
        if not node:
            return 0
        return node.val + self.get_sum(node.left) + self.get_sum(node.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sum = self.get_sum(root)
        self.max_product = 0

        def dfs(node: TreeNode):
            if not node:
                return 0
            left_sum = dfs(node.left)    # Left sub tree sum
            right_sum = dfs(node.right)  # Right sub tree sum
            sub_tree_sum = node.val + left_sum + right_sum
            self.max_product = max(self.max_product,
                                   sub_tree_sum * (tree_sum - sub_tree_sum))
            return sub_tree_sum

        dfs(root)
        return self.max_product % (10**9 + 7)
