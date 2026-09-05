class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop(-1)
            if stack:
                res[i]=stack[-1]-i
            stack.append(i)
        return res
            

            