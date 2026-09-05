class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i=0
        j=0
        min_length=float('inf')
        letters_found=0
        d=dict()
        min_str=''
        for ele in t:
            if ele in d:
                d[ele]+=1
            else:
                d[ele]=1
        while j<len(s):
            if s[j] in d:
                if d[s[j]]>0:
                    letters_found+=1
                d[s[j]]-=1

            while letters_found==len(t):
                if min_length>j-i+1:
                    min_length=j-i+1
                    min_str=s[i:j+1]
                if s[i] in d:
                    d[s[i]]+=1
                    if d[s[i]]>0:
                        letters_found-=1
                i+=1
            j+=1
        return min_str
                
                
            