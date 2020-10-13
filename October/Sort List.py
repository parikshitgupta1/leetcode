class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        l = []
        
        while head:
            l.append(head)
            head = head.next
            
        l.sort(key=lambda x:x.val)
        
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
            
        l[-1].next = None
        return l[0]
