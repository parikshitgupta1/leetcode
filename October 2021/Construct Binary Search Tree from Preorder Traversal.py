from typing import List

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] < preorder[0]: i += 1
            else: break
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
        
