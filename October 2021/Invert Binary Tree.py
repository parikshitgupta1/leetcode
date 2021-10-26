class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root == None:
                return
            else:
                # temp = root
                root.left, root.right = root.right, root.left
                invert(root.right)
                invert(root.left)

            #                 temp = root.left
            #                 root.left = root.right
            #                 root.right = temp
            return root

        return invert(root)
