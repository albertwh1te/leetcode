# 19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def length(self, node):
        l = 0
        while node:
            node = node.next
            l += 1
        return l

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.length(head)
        if length == 1:
            return None
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        length -= n
        while length:
            current = current.next
            length -= 1
            print(current.val)
        current.next = current.next.next
        return dummy.next
