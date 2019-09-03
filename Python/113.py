# 113. Path Sum II

# Given a binary tree and a sum,
# find all root-to-leaf paths
# where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        self.path_sum(root, sum, [])
        return self.result

    def path_sum(self, root: TreeNode, sum: int, path: List[int]):
        if not root:
            return
        if root.left == None and root.right == None:
            if sum == root.val:
                self.result.append(path+[root.val])
        else:
            self.path_sum(root.left, sum-root.val, path+[root.val])
            self.path_sum(root.right, sum-root.val, path+[root.val])
