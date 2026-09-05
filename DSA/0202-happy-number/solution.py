class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(n):
            tot=0
            while(n!=0):
                tot=tot+((n%10)**2)
                n=n//10
            return tot
        d=set()
        while n!=1:
            if n in d:
                return False
            else:
                d.add(n)
            n=sum_squares(n)
        return True