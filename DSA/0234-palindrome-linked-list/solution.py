# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        itr=slow
        while itr:
            n=itr.next
            itr.next=prev
            prev=itr
            itr=n
        itr1,itr2=head,prev
        while itr2:
            if itr1.val!=itr2.val:
                return False
            itr1=itr1.next
            itr2=itr2.next
        return True