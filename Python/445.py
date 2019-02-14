# 445. Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers.
#  The most significant digit comes first and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# Definition for singly-linked list.

# Solution: Use two stack, becasuse stack is LIFO.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = list()
        stack2 = list()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        current = ListNode(-1)
        carry = 0
        while len(stack1) or len(stack2):
            value = carry
            if len(stack1):
                value += stack1.pop()
            if len(stack2):
                value += stack2.pop()
            if value >= 10:
                carry = 1
                value = value % 10
            else:
                carry = 0
            head = ListNode(carry)
            current.val = value
            head.next = current
            current = head
        return current if current.val else current.next
