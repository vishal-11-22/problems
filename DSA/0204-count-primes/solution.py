class Solution:
    def countPrimes(self, n: int) -> int:
        l=[True]*n
        if n==0 or n==1:
            return 0
        l[0]=l[1]=False
        
        for i in range(2,int(n**0.5)+1):
            if i:
                for j in range(i*i,n,i):
                    l[j]=False
        return sum(l)