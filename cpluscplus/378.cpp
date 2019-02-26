// 378. Kth Smallest Element in a Sorted Matrix
// Given a n x n matrix where each of the rows and columns are sorted in ascending order,
//  find the kth smallest element in the matrix.

// Note that it is the kth smallest element in the sorted order,
//  not the kth distinct element.

// Example:

// matrix = [
//    [ 1,  5,  9],
//    [10, 11, 13],
//    [12, 13, 15]
// ],
// k = 8,

// return 13.
// Note:
// You may assume k is always valid, 1 ≤ k ≤ n2.

#include <vector>
#include <queue>
#include <iostream>
using namespace std;

class Solution
{
  public:
    int kthSmallest(vector<vector<int>> &matrix, int k)
    {
        priority_queue<int> pq;
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[i].size(); j++)
            {
                pq.emplace(matrix[i][j]);
            }
        }
        while (pq.size() > k)
        {
            pq.pop();
        }
        return pq.top();
    }
};

int main()
{
    vector<vector<int>> matrix = {
        {1, 5, 9},
        {10, 11, 13},
        {12, 13, 15}};
    Solution s = Solution();
    cout << s.kthSmallest(matrix, 8) << endl;
}