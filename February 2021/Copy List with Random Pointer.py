class Solution:
    def copyRandomList(self, head):
        dummy = Node(-1)
        dummy.next = head
        curr = head
        while curr:
            tmp = Node(curr.val)
            tmp.next = curr.next
            curr.next = tmp
            curr = tmp.next
            
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
            
        curr, nxt = dummy, head
        while nxt:
            curr.next = nxt.next
            curr = nxt
            nxt = curr.next
            
        return dummy.next
