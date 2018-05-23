# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) < 1:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        index = int(len(nums) / 2)
        root = TreeNode(nums[index])
        root.right = self.sortedArrayToBST(nums[index + 1:])
        root.left = self.sortedArrayToBST(nums[0:index])
        return root
