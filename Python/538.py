# 538. Convert BST to Greater Tree

# Given a Binary Search Tree (BST),
#  convert it to a Greater Tree such that every key of the original BST
#  is changed to the original key plus sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root: TreeNode):
        if root == None:
            return
        self.inorder(root.right)
        self.sum += self.val
        root.val = self.sum
        self.inorder(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.inorder(root)
