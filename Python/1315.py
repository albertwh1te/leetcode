# 1315. Sum of Nodes with Even-Valued Grandparent

# Given a binary tree, return the sum of values of nodes with even-valued grandparent.
# (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.


# Example 1:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, parent_value: int, grandparent_value: int) -> int:
            if root == None:
                return 0

            return (
                dfs(root.left, root.val, parent_value)
                + dfs(root.right, root.val, parent_value)
                + (root.val if grandparent_value % 2 == 0 else 0)
            )

        return dfs(root, 1, 1)
