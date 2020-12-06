class Solution:
    def connect(self, root):
        if not root:
            return root
        q = []
        tail = root
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node == tail:
                node.next= None
                if len(q) > 0:
                    tail = q[-1]
                else:
                    None
            else:
                node.next = q[0]
        return root
