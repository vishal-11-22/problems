class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i=0
        j=0
        set_letters=set()
        max_len=float('-inf')
        while j<len(s):
            if s[j] in set_letters:
                while s[j] in set_letters:
                    set_letters.remove(s[i])
                    i+=1
            set_letters.add(s[j])
            max_len=max(max_len,len(set_letters))
            j+=1
        return max_len

            