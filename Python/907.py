# 907. Sum of Subarray Minimums

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

# Since the answer may be large, return the answer modulo 10^9 + 7.

# Example 1:

# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

# Note:

# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000

#  Maintain Stack of Minimums
# Intuition

# For a specific j, let's try to count the minimum of each subarray [i, j].
#  The intuition is that as we increment j++,
#  these minimums may be related to each other.
#  Indeed, min(A[i:j+1]) = min(A[i:j], A[j]).

# Playing with some array like A = [1,7,5,2,4,3,9],
#  with j = 6 the minimum of each subarray [i, j] is B = [1,2,2,2,3,3,9].
#  We can see that there are critical points
#  i = 0, i = 3, i = 5, i = 6
#  where a minimum is reached for the first time when walking left from j.

# Algorithm

# Let's try to maintain an RLE (run length encoding) of these critical points B.
#  More specifically, for the above (A, j),
#  we will maintain stack = [(val=1, count=1), (val=2, count=3), (val=3, count=2), (val=9, count=1)],
#  that represents a run length encoding of the subarray minimums B = [1,2,2,2,3,3,9]. For each j, we want sum(B).

# As we increment j, we will have to update this stack to include the newest element (val=x, count=1).
#  We need to pop off all values >= x before,
#  as the minimum of the associated subarray [i, j] will now be A[j] instead of what it was before.

# At the end, the answer is the dot product of this stack: \sum\limits_{e\text{ } \in \text{ stack}} e\text{.val} * e\text{.count}
# e ∈ stack
# ∑
# ​

#  e.val∗e.count, which we also maintain on the side as the variable dot.

# 对于A中的每一个元素，我们只需要计算出以它为最小值且以它为结束的子串的个数left[i]，然后再计算出以它为最小值且以它为开始的子串的个数right[i]，
# 注意这其中不允许有重复（即一个优先原则，例如1,2,3,1，其中先出现的那个1才是最小值，这样可以避免我们重复计算子串）

from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        return sum(A)


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.sumSubarrayMins)
    test = [3, 1, 2, 4]
    t.equal(17, test)
