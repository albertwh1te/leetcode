# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, r1: 'ListNode', r2: 'ListNode') -> 'ListNode':
        dummy = ListNode(-1)
        current = dummy
        carry = 0
        while r1 or r2:
            value = carry
            if r1:
                value += r1.val
            if r2:
                value += r2.val

            if value >= 10:
                carry = value // 10
                value = value % 10
            else:
                carry = 0

            if r1:
                r1 = r1.next
            if r2:
                r2 = r2.next

            current.next = ListNode(value)
            current = current.next

        if carry:
            current.next = ListNode(1)

        return dummy.next
