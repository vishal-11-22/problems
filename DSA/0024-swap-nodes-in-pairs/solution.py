# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=prev=ListNode(-1)
        itr=head
        while itr:
            if itr.next:
                o_next_add=itr.next.next
                itr.next.next=itr
                prev.next=itr.next
                itr.next=o_next_add
                prev=itr
                itr=itr.next
            else:
                break
        return dummy.next
                

