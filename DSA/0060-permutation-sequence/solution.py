class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        cnt=1
        s=''.join([str(i) for i in range(1,n+1)])
        for i in permutations(s):
            if cnt==k:
                return ''.join(i)
                
            cnt+=1