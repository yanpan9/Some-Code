class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.mins = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins or self.mins[-1]>=x:
          self.mins.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x==self.mins[-1]:
          self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()