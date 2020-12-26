class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        prevNode = head
        currNode = head.next
        prev = None
        head = currNode
        
        while True:
            
            if prev != None:
                prev.next =  currNode
            nextNode = currNode.next
            currNode.next = prevNode
            
            if not nextNode or nextNode.next is None:
                prevNode.next = nextNode
                break
            
            prev = prevNode
            prevNode.next = nextNode
            prevNode = prevNode.next
            currNode = prevNode.next
            
            
        return head
