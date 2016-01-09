/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry=0) {
    if (!l1 && !l2){
      // TODO: simply this base case
      if (carry > 0){
        return new ListNode(carry);
      }
      return NULL; 
    }
    else {
      l1 = l1 ? l1 : new ListNode(0);
      l2 = l2 ? l2 : new ListNode(0);

      int sum = l1->val + l2->val + carry;
      ListNode* n = new ListNode(sum % 10);
      n->next = this->addTwoNumbers(l1->next,l2->next,sum/10);
      return n;
    }
  }
};
/*
* This is a convert to int then back solution, but it does not work because the test case may contain number that exceeded the long limit

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        long num1 = this->listToInt(l1);
        long num2 = this->listToInt(l2);
        long sum = num1 + num2;
        
        //return 0;
        return intToList(sum);
    }
private:
    int listToInt(ListNode* l){
        int num = 0;
        int multiplier = 1;
        while (l->next){
            num += multiplier * l->val;
            multiplier *= 10;
            l = l-> next;
        }
        num += multiplier * l->val;
        return num;
    }
    
    ListNode* intToList(long num){
        if (num < 10){
            return new ListNode(num);
        }
        ListNode* n = new ListNode(num % 10);
        n->next = intToList(num/10);
        return n;
    }
};
*/
