class Solution:
    def subtreeWithAllDeepest(self, root):
        def postorder(root):
            if not root:
                return 0, None
            d1, n1 = postorder(root.left)
            d2, n2 = postorder(root.right)
            if d1 == d2:
                return d1+1, root
            elif d1 > d2:
                return d1+1, n1
            else:
                return d2+1, n2
        d, n = postorder(root)
        return n
