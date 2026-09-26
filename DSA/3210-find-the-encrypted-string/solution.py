class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k=k%len(s)
        print(k)
        res=''
        for i in range(k,len(s)):
            res+=s[i]
        
        for  i in range(0,k):
            res+=s[i]
        return res