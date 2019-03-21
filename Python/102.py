# 102. Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from queue import Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        q1 = Queue()
        q2 = Queue()
        q1.put(root)
        while q1.qsize() > 0:
            tmp = []
            while q1.qsize() > 0:
                node = q1.get()
                tmp.append(node.val)
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            results.append(tmp)
            q1, q2 = q2, q1
        return results
