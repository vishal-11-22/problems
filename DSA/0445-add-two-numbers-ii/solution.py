# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def reverse(itr):
        #     prev=None
        #     while itr:
        #         n=itr.next
        #         itr.next=prev
        #         prev=itr
        #         itr=n
        #     return prev
        # itr1,itr2=reverse(l1),reverse(l2)
        # carry=0
        # dummy=None
        # while itr1 or itr2 or carry:
        #     val1=0;val2=0
        #     if itr1:
        #         val1=itr1.val
                
        #     if itr2:
        #         val2=itr2.val
                
        #     sum_val=val1+val2+carry
        #     if sum_val>=10:
        #         carry=sum_val//10
        #         sum_val=sum_val%10
        #         #carry,sum_val=divmod(val1+val2+carry,10)
        #     n=ListNode(sum_val)
        #     n.next=dummy
        #     dummy=n
        #     if itr1:
        #         itr1=itr1.next
        #     if itr2:
        #         itr2=itr2.next
        # return dummy
        
        st1=[];st2=[]
        while l1:
            st1.append(l1.val)
            l1=l1.next
        while l2:
            st2.append(l2.val)
            l2=l2.next
        mainhead=None
        carry=0
        while st1 or st2 or carry:
            val1=val2=0
            if st1:
                val1=st1.pop(-1)
            if st2:
                val2=st2.pop(-1)

            sum_val=val1+val2+carry
            # if sum_val>=10:
            #     # carry=sum_val//10
            #     # sum_val=sum_val%10
            #     pass
            carry, sum_val = divmod(val1 + val2 + carry, 10)
            n=ListNode(sum_val)
            n.next=mainhead
            mainhead=n
            
        return mainhead
