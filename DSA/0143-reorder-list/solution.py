# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def print_ll(itr):
            while itr:
                print(itr.val,end='->')
                itr=itr.next
        def reverse(node):
            prev=None
            while node:
                n=node.next
                node.next=prev
                prev=node
                node=n
            return prev
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        l2=reverse(slow.next)
        slow.next=None

        itr=l2
        mainhead=head
        print_ll(mainhead)
        while itr:
            nxt_add=mainhead.next
            n=itr
            itr=itr.next
            mainhead.next=n
            n.next=nxt_add
            mainhead=nxt_add
        

        