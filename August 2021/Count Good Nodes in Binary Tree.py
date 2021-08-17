class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, path_max_val: int) -> None:
            if not node:
                return
            self.count += node.val >= path_max_val  
            path_max_val = max(path_max_val, node.val)  
            if node.left:
                dfs(node.left, path_max_val)  
            if node.right:
                dfs(node.right, path_max_val)  

        self.count = 0
        dfs(root, root.val)
        return self.count
