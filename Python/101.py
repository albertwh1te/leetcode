class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.isMirror(left.right, right.left) and self.isMirror(
            left.left, right.right
        )
