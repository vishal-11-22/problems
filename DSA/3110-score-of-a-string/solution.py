class Solution:
    def scoreOfString(self, s: str) -> int:
        i=0
        ans=0
        while i<len(s)-1:
            first=ord(s[i])
            second=ord(s[i+1])
            ans=ans+abs(first-second)
            i+=1
        return ans