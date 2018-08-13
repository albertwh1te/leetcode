# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def has1(self, root):
        if root == None:
            return False
        if root.val == 1:
            return True
        return self.has1(root.right) or self.has1(root.left)

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if not self.has1(root):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root
