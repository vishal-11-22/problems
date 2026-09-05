class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            first_letter=s[i]
            last_letter=s[j]
            if first_letter.isalnum():
                first_letter=first_letter.lower()
            else:
                i+=1
                continue
            if last_letter.isalnum():
                last_letter=last_letter.lower()
            else:
                j-=1
                continue
            if first_letter!=last_letter:
                return False
            i+=1
            j-=1
        return True
            

                    