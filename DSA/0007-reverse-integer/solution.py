class Solution:
    def reverse(self, x: int) -> int:
        sign=0
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        res=0
        while(x):
            res=res*10+x%10
            x=x//10
            if res > 2**31 - 1:
                return 0
        return sign*res