class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        main=dict()
        for i in words[0]:
            if i in main:
                main[i]+=1
            else:
                main[i]=1
        for i in words[1:]:
            current_word=dict()
            for j in i:
                if j in current_word:
                    current_word[j]+=1
                else:
                    current_word[j]=1
            unused=[]
            for word,freq in main.items():
                if word in current_word:
                    if current_word[word]<freq:
                        main[word]=current_word[word]
                else:
                    unused.append(word)
            for i in unused:
                main.pop(i)
        result = []
        for char, count in main.items():
            result.extend([char] * count)
        return result

         