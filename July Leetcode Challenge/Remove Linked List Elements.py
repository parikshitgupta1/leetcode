class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head:
            return
        
        prev, cur = None, head
        
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    head = cur.next
                    cur = head
            else:
                prev = cur
                cur = cur.next
        
        return head
