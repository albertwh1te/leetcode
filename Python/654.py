class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maximum = max(nums)
        left = nums[0:nums.index(maximum)]
        right = nums[nums.index(maximum) + 1:]
        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
