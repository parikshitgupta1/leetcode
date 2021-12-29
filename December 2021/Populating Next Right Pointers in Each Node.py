
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node', next=None) -> 'Node':
        if root is None: return None
        root.next = next
        self.connect(root.left, root.right)
        self.connect(root.right, root.next.left if root.next else None)
        return root
