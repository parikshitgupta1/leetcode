class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None  # Base case

        # If p, q are lesser than root -> traverse left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If p, q are greater than root -> traverse right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both conditions are false, the root is the LCA
        else:
            return root
