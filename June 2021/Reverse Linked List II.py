class Solution:
    def reverseBetween(self, head: ListNode,
                       left: int, right: int) -> ListNode:
        # Base case scenario
        if left == right:
            return head

        node = ptr = ListNode()  # Dummy node before actual linked list
        node.next = head

        # First traverse to node before reversing starts
        for _ in range(1, left):
            ptr = ptr.next

        # Start reversing from next node using three pointer approach
        current_node = ptr.next
        while left < right:
            temp_node = current_node.next
            current_node.next = temp_node.next
            temp_node.next = ptr.next
            ptr.next = temp_node
            left += 1

        return node.next
