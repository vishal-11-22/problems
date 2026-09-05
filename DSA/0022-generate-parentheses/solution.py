class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def generate(open,close,temp):
            if len(temp)==2*n:
                res.append(temp)
                return 
            if open<n:
                generate(open+1,close,temp+'(')
            if close<open:
                generate(open,close+1,temp+')')
        generate(0,0,'')
        return res