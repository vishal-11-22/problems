class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d=dict()
        for i,j in zip(s,t):
            if i in d:
                d[i]+=1
                if d[i]==0:
                    d.pop(i)
            else:
                d[i]=1
            if j in d:
                d[j]-=1
                if d[j]==0:
                    d.pop(j)
                
            else:
                d[j]=-1

        return False if d else True