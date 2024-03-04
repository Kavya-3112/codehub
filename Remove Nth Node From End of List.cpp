class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp= new ListNode(0);
        temp->next=head;
        ListNode* fast=temp;
        ListNode* slow=temp;
        for(int i=0;i<=n;i++){
            fast=fast->next;
        }
        while(fast!=NULL){
            fast=fast->next;
            slow=slow->next;

        }
        ListNode* temp1=slow->next;
        slow->next=slow->next->next;
        delete temp1;
        return temp->next;   
        
    }
};
