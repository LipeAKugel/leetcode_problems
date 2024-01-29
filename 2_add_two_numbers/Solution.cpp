
//Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* l3 = new ListNode();
    ListNode* n1 = l1;
    ListNode* n2 = l2;
    ListNode* n3 = l3;
    int carry = 0;
    
    while (n1 || n2) {
      int x = n1 ? n1->val : 0;
      int y = n2 ? n2->val : 0;

      n3->val = (x + y + carry) % 10;
      carry = (x + y + carry) > 9 ? 1 : 0;

      n1 = n1 ? n1->next : n1;
      n2 = n2 ? n2->next : n2;

      if (n1 || n2) {
        n3->next = new ListNode();
        n3 = n3->next;
      } else if (carry) {
        n3->next = new ListNode(carry);
      }
    }

    return l3;
  }
};