class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        st=s
        s=set()
        cnt=0
        i=0
        j=0
        while j<len(st):
            if st[j] not in s:
                s.add(st[j])
            else:
                while st[j] in s:
                    s.remove(st[i])
                    i+=1
                s.add(st[j])
            if len(s)==3:
                cnt+=1
                s.remove(st[i])
                i+=1
            j+=1
        return cnt