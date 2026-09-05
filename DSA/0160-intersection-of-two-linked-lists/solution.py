# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        itr1=headA
        itr2=headB
        while itr1!=itr2:
            if itr1.next is None and itr2.next is None:
                return 
            if itr1.next is None:
                itr1=headB
            else:
                itr1=itr1.next
            if itr2.next is None:
                itr2=headA
            else:
                itr2=itr2.next

        return itr1
        