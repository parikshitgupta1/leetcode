# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		slow, fast = head, head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				break

		else:
			return None

		curr = head

		while curr != slow:
			curr = curr.next
			slow = slow.next

		return curr
