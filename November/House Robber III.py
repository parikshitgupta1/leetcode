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
