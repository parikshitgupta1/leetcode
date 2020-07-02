class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None: return result
        Q = []
        Q.append(root)
        while len(Q) > 0:
            n = len(Q)
            nodes = []
            for i in range(n):
                node = Q.pop(0)
                nodes.append(node.val)
                if node.left != None: Q.append(node.left)
                if node.right != None: Q.append(node.right)
            result.insert(0, nodes)
        
        return result
