class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=''
        cond=True
        i=0
        while(i<len(s)):
            if cond:
                res+=s[i:i + k][::-1]
                i+=k
                cond=False
            else:
                res=res+s[i:i+k]
                cond=True
                i+=k
        return res