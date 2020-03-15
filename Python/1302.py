# 1302. Deepest Leaves Sum

# Given a binary tree, return the sum of values of its deepest leaves.

# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15


# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def get_depth(node: TreeNode) -> int:
            if node == None:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))

        depth = get_depth(root)

        def count_leaves(root, depth):
            if root == None:
                return 0
            if depth == 1:
                return root.val
            else:
                depth -= 1
                return count_leaves(root.left, depth) + count_leaves(root.right, depth)

        result = count_leaves(root, depth)

        return result

