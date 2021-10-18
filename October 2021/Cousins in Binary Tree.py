# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        ldepth = rdepth = depth = 0
        q.append(root)
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if node.left and node.right:
                    if [node.left.val,node.right.val] == [x,y] or [node.left.val,node.right.val] == [y,x]:
                        return False
                if node.val == x:
                    ldepth = depth
                elif node.val == y:
                    rdepth = depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return ldepth == rdepth
