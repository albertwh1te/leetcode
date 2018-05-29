# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedarray2bst(self, array):
        if array == []:
            return None
        median_index = int(len(array) / 2)
        root = TreeNode(array[median_index])
        print(root.val)
        root.left = self.sortedarray2bst(array[median_index + 1:])
        root.right = self.sortedarray2bst(array[:median_index])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        origin = []
        while head:
            origin.append(head.val)
            head = head.next
        return self.sortedarray2bst(origin)
