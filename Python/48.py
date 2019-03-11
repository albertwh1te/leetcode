class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        # Solution:
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        先上下旋转，再对角线旋转
        """
        length = len(matrix)
        # 上下旋转
        matrix.reverse()
        # 对角线旋转
        for i in range(length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    input1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    Solution().rotate(input1)
    assert (r1 == input1)
    input2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    r2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    Solution().rotate(input2)
    assert (r2 == input2)
