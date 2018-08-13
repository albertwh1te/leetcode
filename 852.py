from util import equal


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


def main():
    equal(Solution().peakIndexInMountainArray([0, 1, 0]), 1)
    equal(Solution().peakIndexInMountainArray([0, 2, 1, 0]), 1)


if __name__ == '__main__':
    main()
