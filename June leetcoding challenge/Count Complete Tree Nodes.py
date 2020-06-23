class Solution:
    def __init__(self) : 
        self.count = 0
    def search(self,root):
        if(root==None) : return 
        self.count+=1
        self.search(root.left)
        self.search(root.right)
    def countNodes(self, root: TreeNode) -> int:
        self.search(root)
        return self.count
