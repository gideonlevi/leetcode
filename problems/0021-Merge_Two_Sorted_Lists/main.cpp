/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;
        ListNode* start = new ListNode();
        ListNode* curr3 = start;

        while (curr1 != NULL && curr2 != NULL) {
            if (curr1->val < curr2->val) {
                curr3->next = new ListNode(curr1->val);
                curr1 = curr1->next;
            } else {
                curr3->next = new ListNode(curr2->val);
                curr2 = curr2->next;
            }
            curr3 = curr3->next;
        }

        while (curr1 != NULL) {
            curr3->next = new ListNode(curr1->val);
            curr1 = curr1->next;
            curr3 = curr3->next;
        }

        while (curr2 != NULL) {
            curr3->next = new ListNode(curr2->val);
            curr2 = curr2->next;
            curr3 = curr3->next;
        }

        // Remove the dummy first node
        ListNode* result = start->next;
        delete start;

        return result;
    }

};
