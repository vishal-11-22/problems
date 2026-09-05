class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        if n==n1:
            return n1
        elif n==n2:
            return n2
        else:
            n-=1
            while(n):
                n1,n2=n2,n1+n2
                n-=1
            return n2