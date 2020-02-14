#  25. Reverse Nodes in k-Group
#  Given a linked list,
#  reverse the nodes of a linked list k at a time and return its modified list.

#  k is a positive integer and is less than or equal to the length of the linked list.
#  If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

#  Example:

#  Given this linked list: 1->2->3->4->5

#  For k = 2, you should return: 2->1->4->3->5

#  For k = 3, you should return: 3->2->1->4->5

#  Note:

#  Only constant extra memory is allowed.
#  You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, previous: ListNode, k: int) -> ListNode:
        """
        reverse ListNode for node to node + k
        for example: 3-2-1-4-5 with 3
        last is 4
        tail is 3(3 will be the tail after the reverse)
        before:  3 2 1 4 5
        stage1:  2 3 1 4 5
        stage2:  1 2 3 4 5
        """
        last = previous
        for i in range(k + 1):
            last = last.next
            if i != k and last == None:
                return None
        tail = previous.next
        current = previous.next.next
        while current != last:
            _next = current.next
            current.next = previous.next
            previous.next = current
            tail.next = _next
            current = _next
        return tail

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        while previous:
            previous = self.reverse(previous, k)
        return dummy.next


if __name__ == "__main__":
    from util import creat_linked_list_from_array, show_linked_list

    t = Solution()
    origin = creat_linked_list_from_array([3, 2, 1, 4, 5])
    show_linked_list(origin)
    show_linked_list(t.reverseKGroup(origin, 2))
    show_linked_list(t.reverseKGroup(origin, 3))
