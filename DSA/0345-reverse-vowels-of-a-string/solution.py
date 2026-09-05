class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        low=0
        high=len(s)-1
        while low<=high:
            if l[low].lower() not in "aeiou":
                low+=1
            elif l[high].lower() not in "aeiou":
                high-=1
            else:
                l[low],l[high]=l[high],l[low]
                low+=1
                high-=1
        return ''.join(l)

