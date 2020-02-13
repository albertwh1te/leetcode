# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        while a and b:
            if a.val > b.val:
                current.next = ListNode(b.val)
                b = b.next
            else:
                current.next = ListNode(a.val)
                a = a.next
            current = current.next

        if a:
            current.next = a
        if b:
            current.next = b

        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.merge(lists[0], lists[1])

        mid = len(lists) >> 1
        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)
