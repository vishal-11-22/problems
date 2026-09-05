class MyStack:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        for i in range(len(self.st1)-1):
            ele=self.st1.pop(0)
            self.st1.append(ele)
        ele=self.st1.pop(0)
        return ele

    def top(self) -> int:
        return self.st1[-1]

    def empty(self) -> bool:
        if len(self.st1)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()