class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        tn=TreeNode(preorder[0])
        l=[]
        r=[]
        for i in preorder:
            if i<preorder[0]:
                l.append(i)
            elif i>preorder[0]:
                r.append(i)
        tn.left=self.bstFromPreorder(l)
        tn.right=self.bstFromPreorder(r)
        return tn
