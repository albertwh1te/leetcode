# 160. Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

# Solution
# 1) Get count of the nodes in the first list, let count be c1.
# 2) Get count of the nodes in the second list, let count be c2.
# 3) Get the difference of counts d = abs(c1 – c2)
# 4) Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
# 5) Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l_a = get_length(headA)
        l_b = get_length(headB)
        diff = abs(l_a - l_b)

        # move to same start position
        if l_a > l_b:
            while diff:
                headA = headA.next
                diff -= 1
        if l_a < l_b:
            while diff:
                headB = headB.next
                diff -= 1

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None


def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
