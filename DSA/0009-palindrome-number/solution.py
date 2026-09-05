class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            temp=x
            rev=0
            while(x):
                rem=x%10
                rev=rev*10+rem
                x=x//10
            
            return temp==rev
