"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        itr=head
        stack=[]
        while itr:
            if itr.child:
                if itr.next:
                    stack.append(itr.next)
                itr.child.prev=itr
                itr.next=itr.child
                itr.child=None
            if itr.next is None:
                if stack:
                    n=stack.pop(-1)
                    n.prev=itr
                    itr.next=n
            itr=itr.next
        return head


