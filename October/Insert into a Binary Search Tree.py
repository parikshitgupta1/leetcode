class Solution:
	def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
		if not root:
			root = TreeNode(val = val)
		elif root.val > val:
			root.left = self.insertIntoBST(root.left, val)
		else:
			root.right = self.insertIntoBST(root.right, val)
		return root
