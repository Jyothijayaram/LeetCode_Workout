# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos=0
        d=head
        count=1
        while head is not None:
            pos+=1
            head=head.next
        # print(pos)
        pos=(pos//2)+1
        while count!=pos:
            count+=1
            d=d.next
        return d
        