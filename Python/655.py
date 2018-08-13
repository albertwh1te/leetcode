# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def depthFirstSearch(self, root):
        if root == None:
            return 0
        return 1 + max(self.depthFirstSearch(root.left), self.depthFirstSearch(root.right))

    def levelPrint(self, root, level, position, results):
        if root == None:
            return results
        distance = 2 ** (self.height - level - 1)
        results[level - 1][position] = str(root.val)
        results = self.levelPrint(
            root.left, level + 1, position - distance, results)
        results = self.levelPrint(
            root.right, level + 1, position + distance, results)
        return results

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.height = self.depthFirstSearch(root)
        self.width = 2 ** self.height - 1
        results = [["" for _ in range(self.width)] for _ in range(self.height)]
        self.levelPrint(root, 1, int(self.width / 2), results)
        return results


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.printTree)

    theroot1 = TreeNode(1)
    theroot1.left = TreeNode(2)
    r1 = [["", "1", ""],
          ["2", "", ""]]
    t.equal(r1, theroot1)

    theroot2 = TreeNode(1)
    theroot2.left = TreeNode(2)
    theroot2.right = TreeNode(3)
    theroot2.left.right = TreeNode(4)
    r2 = [["", "", "", "1", "", "", ""],
          ["", "2", "", "", "", "3", ""],
          ["", "", "4", "", "", "", ""]]
    t.equal(r2, theroot2)
