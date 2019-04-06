# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list.
#  The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        c1 = l1
        c2 = l2
        while c1 and c2:
            if c1.val <= c2.val:
                current.next = ListNode(c1.val)
                c1 = c1.next
            else:
                current.next = ListNode(c2.val)
                c2 = c2.next
            current = current.next

        if c1:
            current.next = c1

        if c2:
            current.next = c2

        return dummy.next
