# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# Note:

# The number of nodes in the given list will be between 1 and 100.
#  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# case 1  [1,2,3,4,5]
# fast : 1,3,5
# slow : 1,2,3
# return slow

# case 2 [1,2,3,4,5,6]
# fast : 1,3,5
# slow: 1,2,3
# return  slow.next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while 1:
            if not fast.next:
                # case 1
                return slow
            if not fast.next.next:
                # case 2
                return slow.next

            slow = slow.next
            fast = fast.next.next
