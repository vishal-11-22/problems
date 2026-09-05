class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt=0
        for i in words:
            used=[i for i in chars]
            can_form=True
            for j in i:
                if j not in used:
                    can_form=False
                    break
                else:
                    used.remove(j)
            if can_form:
                cnt+=len(i)
    
        return cnt       
        