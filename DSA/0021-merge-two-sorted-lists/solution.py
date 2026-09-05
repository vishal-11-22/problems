# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itr1=list1
        itr2=list2
        tail=head=None
        if not list1:
            return list2
        if not list2:
            return list1
        while itr1 and itr2:
            if itr1.val<itr2.val:
                if not head:
                    head=ListNode(itr1.val)
                    tail=head
                else:
                    tail.next=ListNode(itr1.val)
                    tail=tail.next
                itr1=itr1.next
            else:
                if not head:
                    head=ListNode(itr2.val)
                    tail=head
                else:
                    tail.next=ListNode(itr2.val)
                    tail=tail.next
                itr2=itr2.next
        while itr1:
            tail.next=ListNode(itr1.val)
            tail=tail.next
            itr1=itr1.next
        while itr2:
            tail.next=ListNode(itr2.val)
            tail=tail.next
            itr2=itr2.next
        return head


            