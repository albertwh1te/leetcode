from util import equal


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return A.index(max(A))
        left = 0
        right = len(A)
        while 1:
            mid = (right + left) >> 1
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] > A[mid]:
                right = mid + 1
            else:
                left = mid


def main():
    equal(Solution().peakIndexInMountainArray([0, 1, 0]), 1)
    equal(Solution().peakIndexInMountainArray([0, 2, 1, 0]), 1)


if __name__ == '__main__':
    main()
