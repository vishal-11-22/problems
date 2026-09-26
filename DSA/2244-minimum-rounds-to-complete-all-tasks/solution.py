class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        hashmap=dict()
        for i in tasks:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        cnt=0
        for i in hashmap.values():
            if i==1:
                return -1
            if i%3==0:
                cnt+=i//3
                continue
            else:
                if i%3==1:
                    cnt+=(i-4)//3
                    i-=4
                    cnt+=2
                    i=0
                if i>=2 and (i%3)%2==0:
                    cnt+=i//3
                    cnt+=1
                    i=0
                

            
            
        return cnt