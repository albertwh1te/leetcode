/**
 * Definition for singly-linked list.
 */
struct ListNode
{
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
class Solution
{
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
  {
    ListNode dummy = ListNode(0);
    ListNode *current = &dummy;
    int value = 0;
    int carry = 0;
    while (l1 || l2)
    {
      value = carry;
      if (l1)
      {
        value += l1->val;
      }
      if (l2)
      {
        value += l2->val;
      }
      if (value >= 10)
      {
        value = value % 10;
        carry = 1;
      }
      else
      {
        carry = 0;
      }

      if (l1)
      {
        l1 = l1->next;
      }
      if (l2)
      {
        l2 = l2->next;
      }
      current->next = new ListNode(value);
      current = current->next;
    }
    if (carry)
    {
      current->next = new ListNode(1);
    }
    return dummy.next;
  }
};