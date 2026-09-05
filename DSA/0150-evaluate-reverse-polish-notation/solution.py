class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*','/']:
                op=tokens[i]
                if len(stack)>1:
                    ele1=stack.pop(-1)
                    ele2=stack.pop(-1)
                if op=='+':
                    stack.append(ele1+ele2)
                elif op=='*':
                    stack.append(ele1*ele2)
                elif op=='/':
                    stack.append(int(ele2/ele1))
                elif op=='-':
                    stack.append(ele2-ele1)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]