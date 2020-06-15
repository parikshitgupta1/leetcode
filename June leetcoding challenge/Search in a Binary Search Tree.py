class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # if root is None:
        #     return
        # if root.val == val:
        #     return root
        # if root.val > val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)
        ## *  Solution 1 above (Recursive)
        ## *  Soluton 2 Below (Iterative)
        trav = root
        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left
