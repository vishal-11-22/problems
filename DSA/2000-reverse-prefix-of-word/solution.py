class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in  word:
            return word
        idx=''
        for i in range(len(word)):
            idx+=word[i]
            if word[i]==ch:
                break
        return idx[::-1]+word[i+1:]
            
                
        
        