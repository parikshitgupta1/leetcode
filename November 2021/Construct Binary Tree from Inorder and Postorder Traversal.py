# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        val_index_dict = { num:idx for idx, num in enumerate(inorder) }
        
        def helper( left, right):
            
            if left > right:
                return None         #empty node as leaf node's child
            
            else:
                #postorder traversal: Left, Right, Center
                root = TreeNode( postorder.pop() )
                
                mid = val_index_dict[ root.val ]
                
                root.right = helper( mid+1, right)
                root.left = helper( left, mid-1 )
                return root
        
        ## Top-down rebuild binary tree with definition
        return helper( left = 0, right = len(inorder)-1 )
        
