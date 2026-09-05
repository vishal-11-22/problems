# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        itr1,itr2=l1,l2
        carry=0
        while itr1 or itr2 or carry:
            if itr1:
                val1=itr1.val
                itr1=itr1.next
            else:
                val1=0
            if itr2:
                val2=itr2.val
                itr2=itr2.next
            else:
                val2=0
            ans=val1+val2+carry
            carry=ans//10
            ans=ans%10
            if res is None:
                res=ListNode(ans)
            else:
                ptr=res
                while ptr.next:
                    ptr=ptr.next
                ptr.next=ListNode(ans)

        return res

        