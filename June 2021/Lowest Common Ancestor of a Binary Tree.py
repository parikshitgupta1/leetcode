class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if not root:
            return None

        # If root is either p, q; root becomes LCA
        if root == p or root == q:
            print('yay')
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # Traverse left
        right = self.lowestCommonAncestor(root.right, p, q)  # Traverse right

        # Both p, q are not null, the current node is LCA
        if left and right:
            return root
        # Otherwise check left or right sub trees respectively
        if left:
            return left
        else:
            return right
