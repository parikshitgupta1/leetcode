class Solution:
    def reverseKGroup(self, head, k):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return self.reverse(head, k, length)
    
    def reverse(self, head, k, length):
        if not head or length < k:
            return head
        prev, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head.next = self.reverse(cur, k, length-k)
        return prev
