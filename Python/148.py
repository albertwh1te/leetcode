# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        fast = head
        slow = head
        if fast != None and fast.next != None:
            current = slow
            fast = fast.next.next
            slow = slow.next
        current.next = None
        return self.merge(self.sortList(slow), self.sortList(head))

    def merge(self, a, b) -> ListNode:
        """
        merge two sorted linked list
        """
        dummy = ListNode()
        current = dummy
        while a and b:
            if a.val >= b.val:
                current.next = b
                b = b.next
            else:
                current.next = a
                a = a.next
            current = current.next
        if a:
            current.next = a
        if b:
            current.next = b
        return dummy.next
