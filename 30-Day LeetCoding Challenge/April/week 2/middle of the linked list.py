
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getCount(temp): 
        count = 0 
  
        while (temp): 
            count += 1
            temp = temp.next
        return count 

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = getCount(head)
        mid = 0 + (l-0)/2
        if l % 2 != 0:
            for i in range(int(mid)):
                head = head.next
            return head
        else:
            for i in range(int(mid)):
                head = head.next
            return head
