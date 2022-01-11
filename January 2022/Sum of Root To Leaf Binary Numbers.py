# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        nums=[]
        strs=''
        def pathsum(p,strs):
            if p is None:
                return
            
            strs=strs+str(p.val)
            
            if not p.left and not p.right:
                nums.append(int(strs,2))
                strs=''
                
            pathsum(p.left,strs)
            pathsum(p.right,strs)
        
        pathsum(root,strs)
        ans=sum(nums)
        return ans
        
