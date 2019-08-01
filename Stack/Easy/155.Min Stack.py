class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if self.stack2:
            if self.stack2[-1] > x:
                self.stack2.append(x)
            else:
                self.stack2.append(self.stack2[-1])
        else:
            self.stack2.append(x)

    def pop(self) -> None:
        if self.stack1:
            self.stack1.pop()
            self.stack2.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    print(minStack.getMin())

    minStack.pop()

    print(minStack.top())

    print(minStack.getMin())
