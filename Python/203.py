# 203. Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        previous = dummy
        current = head
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
        return dummy.next
