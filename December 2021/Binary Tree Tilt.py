# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        def traverse(node, res):
            if not node:
                return 0
            
            left_sum = traverse(node.left, res)
            right_sum = traverse(node.right, res)
            res[0] += abs(left_sum-right_sum)
            
            return left_sum + right_sum + node.val
        
        res = [0]
        traverse(root, res)
        return res[0]
        
