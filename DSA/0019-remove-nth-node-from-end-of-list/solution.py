# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        itr1=head
        itr2=head
        for _ in range(n):
            itr2=itr2.next
        if itr2 is None:
            return head.next
        while itr2.next:
            itr1=itr1.next
            itr2=itr2.next
        itr1.next=itr1.next.next
        return head
        