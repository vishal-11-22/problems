# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        fast=head
        slow=head
        prev=head
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next

        
        if prev.next:
            prev.next=prev.next.next
        else:
            prev.next=None
     
       
        return head