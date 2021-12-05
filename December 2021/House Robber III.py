# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        
        def helper(root):
            
            if root is None:
                return [0,0]
            
            x = helper(root.left)
            y = helper(root.right)
            
            
            return [root.val+x[1]+y[1],max(x)+max(y)]
        
        ans = helper(root)
        return max(ans)
        
