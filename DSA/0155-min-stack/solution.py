class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or self.minstack[-1]>=value:
            self.minstack.append(value)

    def pop(self) -> None:
        if self.stack and self.minstack and self.stack[-1]==self.minstack[-1]:
            self.minstack.pop(-1)
        ele=self.stack.pop(-1)
        return ele

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()