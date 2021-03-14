class Solution:
    def swapNodes(self, head, k):
        n = 0
        beg = head
        while beg:
            if n == k-1: l = beg
            beg = beg.next
            n += 1
        
        r = head
        for m in range(n-k):
            r = r.next
                
        l.val, r.val = r.val, l.val
        return head
