class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.path(root,low,high)
    
    def path(self,node,l,h):
        if not node:
            return None
        
        node.left=self.path(node.left,l,h)
        node.right=self.path(node.right,l,h)
        
        if(node.val<l):
            return node.right
        elif node.val>h:
            return node.left
        else:
            return node
