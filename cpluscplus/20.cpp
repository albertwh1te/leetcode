#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> s_stack;

        unordered_map<char, char> umap;
        umap['('] = ')';
        umap['['] = ']';
        umap['{'] = '}';

        char *s_array = new char[s.length() + 1];
        strcpy(s_array, s.c_str());


        for (int i = 0; i < s.size(); i++) {
            if (s_array[i] == '(' or s_array[i] == '[' or s_array[i] == '{') {
                s_stack.push(umap[s_array[i]]);
            } else if (s_stack.size() > 0 and s_array[i] == s_stack.top()) {
                s_stack.pop();
            } else {
                return false;
            }
        }
        return s_stack.size() == 0;
    }
};


int main() {
    cout << "leetcode 20 " << endl;
    string s;
    bool result;
//    Example 1:
//
//    Input: s = "()"
//    Output: true
//    Example 2:
//
//    Input: s = "()[]{}"
//    Output: true
//    Example 3:
//
//    Input: s = "(]"
//    Output: false
//    Example 4:
//
//    Input: s = "([)]"
//    Output: false
//    Example 5:
//
//    Input: s = "{[]}"
//    Output: true
    s = "()";
    cout << s << Solution().isValid(s) << endl;
    s = "()[]{}";
    cout << s << Solution().isValid(s) << endl;
    s = "(]";
    cout << s << Solution().isValid(s) << endl;
    s = "([)]";
    cout << s << Solution().isValid(s) << endl;
    s = "{[]}";
    cout << s << Solution().isValid(s) << endl;
    s = "{";
    cout << s << Solution().isValid(s) << endl;
    s = ")";
    cout << s << Solution().isValid(s) << endl;
}
