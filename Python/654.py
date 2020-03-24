class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maximum = float("-inf")
        max_index = 0
        for index, value in enumerate(nums):
            if value > maximum:
                maximum = value
                max_index = index
        left = nums[0:max_index]
        right = nums[max_index + 1 :]
        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
