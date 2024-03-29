# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode, ancestors = []) -> int:
        if root == None:
            return 0
        
        curr = 0
        if ancestors:
            curr = max(abs(root.val - max(ancestors)), abs(root.val - min(ancestors)))
        
        ancestors.append(root.val)
        left = self.maxAncestorDiff(root.left)
        right = self.maxAncestorDiff(root.right)
        ancestors.pop()
        
        return max([curr, left, right])
