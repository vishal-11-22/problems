class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l={'a','e','i','o','u'}
        n=len(s)
        cnt_vowels=0
        for i in range(k):
            if s[i] in l:
                cnt_vowels+=1
        max_count_vowels=cnt_vowels
        low=0
        high=k
        while(high<n):
            if s[low] in l:
                cnt_vowels-=1
            if s[high] in l:
                cnt_vowels+=1
            max_count_vowels=max(max_count_vowels,cnt_vowels)
            low+=1
            high+=1
        return max_count_vowels