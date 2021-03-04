class Solution:
    def getIntersectionNode(self, headA, headB):
        currA, currB = headA, headB
        
        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next
            
        return currA
