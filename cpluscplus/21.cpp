//21. Merge Two Sorted Lists
//Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *dummy = new ListNode(0);
        ListNode *current = dummy;
        ListNode *c1 = l1;
        ListNode *c2 = l2;
        while (c1 != nullptr and c2 != nullptr) {
            if (c1->val <= c2->val) {
                current->next = c1;
                c1 = c1->next;
            } else {
                current->next = c2;
                c2 = c2->next;
            };
            current = current->next;
        }

        if (c1 != nullptr) {
            current->next = c1;
        }
        if (c2 != nullptr) {
            current->next = c2;
        }
        return dummy.next;
    }
};



