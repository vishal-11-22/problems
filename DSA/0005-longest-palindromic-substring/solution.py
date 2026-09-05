class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        max_str=''
        for i in range(len(s)):
            k=j=i
            while(j>=0 and k<len(s) and s[j]==s[k]):
                if k-j+1>max_len:
                    max_len=k-j+1
                    max_str=s[j:k+1]
                j-=1
                k+=1
            j=i;k=i+1
            while(j>=0 and k<len(s) and s[j]==s[k]):
                if k-j+1>max_len:
                    max_len=k-j+1
                    max_str=s[j:k+1]
                j-=1
                k+=1
        return max_str
            