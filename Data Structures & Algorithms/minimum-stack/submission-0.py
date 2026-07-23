class MinStack:

    def __init__(self):
        self.stack = list()
        self.stackMin = list()

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.stackMin:
            if self.stackMin[-1] > value:
                self.stackMin.append(value)
            else:
                self.stackMin.append(self.stackMin[-1])
        else:
            self.stackMin.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()