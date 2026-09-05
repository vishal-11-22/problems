# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=dummy=ListNode()
        itr=head
        while itr:
            n=itr
            itr=itr.next
            if not itr or n.val!= itr.val:
                p.next=n
                p=n
            else:
                while itr and n.val==itr.val:
                    itr=itr.next
        p.next=None
        return dummy.next

       