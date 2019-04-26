// 4. Median of Two Sorted Arrays
#include <iostream>
#include <vector>
using namespace std;

int findKth(vector<int> &a, int a_start, int a_end, vector<int> &b, int b_start, int b_end, int k)
{
    // corner case
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
        return min(a[a_start], b[b_start]);
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
    return findKth(a, a_start, a_end, b, b_start + pa, b_end, k - pa);
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
            return a;
        }
        int b = findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2);
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