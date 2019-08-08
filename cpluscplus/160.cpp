/**
 * Definition for singly-linked list.
 */
#include <iostream>
using namespace std;
#define NULL 0
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int length(ListNode *head)
{
    int length = 0;
    while (head)
    {
        head = head->next;
        ++length;
    }
    return length;
}

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        int lengthA = length(headA);
        int lengthB = length(headB);
        int diff = abs(lengthA - lengthB);
        while (diff)
        {
            if (lengthA > lengthB)
            {
                headA = headA->next;
            }
            else
            {
                headB = headB->next;
            }
            --diff;
        }
        while (headA && headB)
        {
            if (headA == headB)
            {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
};
