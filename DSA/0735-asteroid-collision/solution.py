class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if i<0:
                    while stack and (stack[-1]>0 and stack[-1]<abs(i)):
                        stack.pop(-1)
                    if not stack or stack[-1]<0:
                        stack.append(i)
                        continue
                    if stack and  abs(stack[-1])==abs(i):
                        stack.pop(-1)
                        # continue
                else:
                    stack.append(i) 
        return stack            