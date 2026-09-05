# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right or head is None:
            return head
        if left==1:
            last=itr=head
        else:
            ptr=head
            for _ in range(left-2):
                ptr=ptr.next
            last=itr=ptr.next
        prev=None
        for _ in range(right-left+1):
            n=itr.next
            itr.next=prev
            prev=itr
            itr=n
        if left==1:
            head=prev
        else:
            ptr.next=prev
        last.next=itr
        return head
