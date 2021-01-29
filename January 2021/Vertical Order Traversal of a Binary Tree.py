class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def bfs(root, x, y):
            if not root:
                return
            res.append(((x, y), root.val))
            bfs(root.left, x - 1, y + 1)
            bfs(root.right, x + 1, y + 1)

        bfs(root, 0, 0)
        res.sort()
        print(res)
        groups = collections.defaultdict(list)
        for k, v in res:
            x, _ = k
            groups[x].append(v)
        ans = []
        for k in sorted(list(groups.keys())):
            ans.append(groups[k])

        return ans
