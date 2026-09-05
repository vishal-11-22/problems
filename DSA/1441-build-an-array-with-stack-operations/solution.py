class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        res=[]
        for i in range(1,(n+1)):
            stack.append(i)
            res.append("Push")
            if stack and target and stack[-1]!=target[0]:
                res.append("Pop")
                
            if target and stack[-1]==target[0]:
                target.pop(0)
                if len(target)==0:
                    break

        return res