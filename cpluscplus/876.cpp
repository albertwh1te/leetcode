struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// use two pointer
// case 1 even ,there is two median , return slow.next
// case 2 odd, return the slow

class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        if (!head || !head->next)
        {
            return head;
        }
        ListNode *slow = head;
        ListNode *fast = head;
        while (1)
        {
            if (!fast->next)
            // case 2 odd lined list
            {
                return slow;
            }
            if (!fast->next->next)
            // case 2 even lined list
            {
                return slow->next;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
    }
};