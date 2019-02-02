# 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # TODO: write solution with O(1) space complexity and O(n) time complexity
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        current = head
        while current:
            if stack.pop() != current.val:
                return False
            else:
                current = current.next
        return True
