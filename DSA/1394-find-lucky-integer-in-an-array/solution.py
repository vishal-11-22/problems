class Solution:
    def findLucky(self, arr: list[int]) -> int:
        hashmap=dict()
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        cnt=None
        for i,j in hashmap.items():
            if i==j:
                if cnt==None:
                    cnt=j
                elif j>cnt:
                    cnt=j
        if cnt==None:
            return -1
        
        return cnt