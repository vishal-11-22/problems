class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s,low,high):
            while low<high:
                if s[low]!=s[high]:
                    return False
                low+=1
                high-=1
            return True
        low=0
        high=len(s)-1
        er=0
        while(low<high):
            if s[low]!=s[high]:
                return valid(s,low+1,high) or valid(s,low,high-1)
            
            low+=1
            high-=1
        return True