# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Union


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_index = {v: i for i, v in enumerate(inorder)}

        def help(
            inorder_start: int,
            inorder_end: int,
            postorder_start: int,
            postorder_end: int,
        ) -> Union[TreeNode, None]:
            if inorder_end - inorder_start < 1:
                return None
            root_value = postorder[postorder_end - 1]
            root_index = inorder_index[root_value]
            root = TreeNode(root_value)
            left_length = root_index - inorder_start
            right_length = inorder_end - root_index
            if right_length > 0:
                root.right = help(
                    root_index + 1,
                    inorder_end,
                    postorder_end - right_length,
                    postorder_end - 1,
                )

            if left_length > 0:
                root.left = help(
                    inorder_start,
                    inorder_start + left_length,
                    postorder_start,
                    postorder_start + left_length,
                )
            return root

        return help(0, len(inorder), 0, len(postorder))

