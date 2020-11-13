class Solution:
    def connect(self, root: 'Node', next=None) -> 'Node':
        if root is None: return None
        root.next = next
        self.connect(root.left, root.right)
        self.connect(root.right, root.next.left if root.next else None)
        return root
