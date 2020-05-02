# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return len(arr)==0
        def helper(root,index,n):
            if not root:
                return False
            if not root.right and not root.left and root.val==arr[index] and index==n-1 :
                return True

            if root.val==arr[index] and index<n-1:
                return helper(root.left,index+1,n) or helper(root.right,index+1,n)
            return False
        return helper(root,0,len(arr))
        
