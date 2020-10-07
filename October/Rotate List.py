class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        prev = None
        cur = head
        
        if not head or not head.next:
            return head
        
        # first get length of list
        length = 0
        while cur:
            length += 1
            cur = cur.next
        cur = head
        
        for i in range(k % length):
            while cur.next:
                prev = cur
                cur = cur.next
            cur.next = head
            head = cur
            prev.next = None
        return head
