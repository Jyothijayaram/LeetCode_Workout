# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newnode=None
        while head!=None:
            nextnode=head.next
            head.next=newnode
            
            newnode=head
            head=nextnode
        return newnode
        
        