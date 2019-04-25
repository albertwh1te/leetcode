// 4. Median of Two Sorted Arrays
#include <iostream>
#include <vector>
using namespace std;

// A = {1，3，5，7}；B = {2，4，6，8，9，10}；
// 如果要求第7个小的数，
// A数列的元素个数为4，
// B数列的元素个数为6；
// k/2 = 7/2 = 3，
// 而A中的第3个数A[2]=5；
// B中的第3个数B[2]=6；
// 而A[2]<B[2]；
// 则A[0]，A[1]，A[2]中必然不可能有第7个小的数。
// 因为A[2]<B[2]，
// 所以比A[2]小的数最多可能为A[0],
//  A[1], B[0], B[1]
// 这四个数，
// 也就是说A[2]最多可能是第5个大的数，
// 由于我们要求的是getKth(A, B, 7)；
// 现在就变成了求getKth(A', B, 4)；
// 即A' = {7}；
// B不变，求这两个数列的第4个小的数，因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。
int findKth(vector<int> &a, int a_start, int a_end, vector<int> &b, int b_start, int b_end, int k)
{
    if (a_end - a_start > b_end - b_start)
    {
        return findKth(b, b_start, b_end, a, a_start, a_end, k);
    }
    if (a_end < a_start)
    {
        return b[k - 1];
    }
    if (k == 1)
    {
        return min(a[0], b[0]);
    }
    int pa = min(k / 2, a_end - a_start + 1);
    int pb = k - pa;
    if (a[a_start + pa - 1] == b[b_start + pb - 1])
    {
        return a[a_start + pa - 1];
    }
    if (a[a_start + pa - 1] < b[b_start + pb - 1])
    {
        return findKth(a, a_start + pa, a_end, b, b_start, b_end, k - pa);
    }

    if (a[a_start + pa - 1] > b[b_start + pb - 1])
    {
        return findKth(a, a_start, a_end, b, b_start + pa, b_end, k - pa);
    }
}

class Solution
{
  public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        double a = (double)findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2 + 1);
        if (total % 2)
        {
            cout << "odd:" << a << "total" << total << endl;
            return a;
        }

        int b = findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2);
        cout << "even :" << b << endl;
        return (a + b) * 0.5;
    }
};

int main()
{
    vector<int> test1 = {1, 3};
    vector<int> test2 = {2};
    Solution s = Solution();
    double answer = s.findMedianSortedArrays(test1, test2);
    cout << "should be 2.0: and get " << answer << endl;
    test1 = {1, 2};
    test2 = {3, 4};
    double answer2 = s.findMedianSortedArrays(test1, test2);
    cout << "should be 2.5:" << answer2 << endl;
    return 0;
}