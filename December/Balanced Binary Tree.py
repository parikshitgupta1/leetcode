class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        def helper(root):
            
            if root is None:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)
        
            if left_height == None or right_height == None:
                return None
            
            if abs(left_height - right_height) > 1:
                return None

            return max(left_height,right_height)+1    
        
        
        return True if helper(root) != None else False
