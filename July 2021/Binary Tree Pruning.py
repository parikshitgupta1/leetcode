class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def has_one(root: TreeNode) -> bool:
            if not root:
                return False
            left = has_one(root.left)  
            right = has_one(root.right) 
            if not left:
                root.left = None
            if not right:
                root.right = None
            return root.val == 1 or left or right
        if not has_one(root):
            root = None
        return root
