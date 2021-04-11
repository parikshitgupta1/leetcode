class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = []
        q.append(root)
        sum = 0
        while len(q) != 0:
            length = len(q)
            sum = 0
            for i in range(length):
                cur = q.pop(0)
                sum += cur.val
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        return sum
