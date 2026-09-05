# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head

       
        while head and head.val == val:
            head = head.next

        itr = head
        prev = None

        while itr:
            if itr.val == val:
                prev.next = itr.next
            else:
                prev = itr
            itr = itr.next

        return head
