class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res=[]
        def dfs(index,combination):
            if index==len(digits):
                res.append(combination)
                return 
            for i in phone[digits[index]]:
                dfs(index+1,combination+i)
        dfs(0,'')
        return res 
        


        