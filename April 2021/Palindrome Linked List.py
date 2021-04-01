class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        current = head
        if head == None :
           return True
        else:
            while current:
                result.append(str(current.val))
                current = current.next
        return result == result[::-1]
