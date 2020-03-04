# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_index = {v: i for i, v in enumerate(inorder)}

        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            if inorder_end - inorder_start < 1:
                return None
            root_value = preorder[preorder_start]
            root = TreeNode(root_value)
            root_index = inorder_index[root_value]
            left_length = root_index - inorder_start
            right_length = inorder_end - root_index
            if left_length > 0:
                root.left = helper(
                    preorder_start + 1,
                    preorder_start + left_length,
                    inorder_start,
                    inorder_start + left_length,
                )
            if right_length > 0:
                root.right = helper(
                    preorder_start + left_length + 1,
                    preorder_end,
                    root_index + 1,
                    inorder_end,
                )
            return root

        return helper(0, len(preorder), 0, len(inorder))
