# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast != None:

            if fast.next == None:
                return slow
            fast = fast.next.next
            slow = slow.next

        return slow
