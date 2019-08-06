/**
 * Definition for singly-linked list.
 */

#define NULL 0
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        if (!head)
        {
            return head;
        }
        ListNode tmp = ListNode(-1);
        ListNode *dummy = &tmp;
        dummy->next = head;
        ListNode *previous = dummy;
        ListNode *current = head;
        while (current)
        {
            if (current->val == val)
            {
                previous->next = current->next;
            }
            else
            {
                previous = previous->next;
            }
            current = current->next;
        }
        return dummy->next;
    }
};