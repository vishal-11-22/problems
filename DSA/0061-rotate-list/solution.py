# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        length=1
        itr=head
        while itr.next:
            length+=1
            itr=itr.next
        k=k%length
        ptr=head
        for _ in range(length-k-1):
            ptr=ptr.next
        itr.next=head
        head=ptr.next
        ptr.next=None
        return head

        





        
        
        