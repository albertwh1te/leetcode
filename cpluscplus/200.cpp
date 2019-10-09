#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int columns = 0;
    int rows = 0;

    void infect(vector<vector<char>> &grid, int x, int y)
    {
        if (y >= columns || x >= rows || y < 0 || x < 0 || grid[y][x] != '1')
        {
            return;
        }
        grid[y][x] = '2';
        infect(grid, x, y + 1);
        infect(grid, x, y - 1);
        infect(grid, x + 1, y);
        infect(grid, x - 1, y);
    }

    int numIslands(vector<vector<char>> &grid)
    {
        if (grid.size() == 0 || grid[0].size() == 0)
        {
            return 0
        }
        int count = 0;
        columns = grid.size();
        rows = grid[0].size();
        for (int y = 0; y < columns; y++)
        {
            for (int x = 0; x < rows; x++)
            {
                if (grid[y][x] == '1')
                {
                    count++;
                    infect(grid, x, y);
                }
            }
        }
        return count;
    }
};

int main()
{
    vector<vector<char>> grid = {
        {'1', '1', '1', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'},
    };
    int target = 3;
    Solution s = Solution();
    int answer = s.numIslands(grid);
    cout << answer << endl;
    return 0;
}