#include <stack>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        while(l1){
            s1.push(l1->val);
            l1 = l1->next;
        }
        while(l2){
            s2.push(l2->val);
            l2 = l2->next;
        }
        ListNode *current;
        ListNode *head;
        int value = 0;
        int carry = 0;
        while(s1.size()||s2.size()){
            value = carry;
            if(s1.size()){
                value += s1.top();
                s1.pop();
            }
            if(s2.size()){
                value += s2.top();
                s2.pop();
            }
            if(value >=10){
                value %= 10;
                carry = 1;
            } else{
                carry = 0;
            }
            current->next =  new ListNode(value);
            current = current->next;
        }
        head = new ListNode(carry);
        head->next = current;
        current->val = value;
        current = head;
        return current->val ? current :current->next;
    }
};