class MinStack(object):
    def __init__(self):
        self.st = []

    def push(self, val):
        if not self.st:
            self.st.append((val, val))
        else:
            mini = min(val, self.st[-1][1])
            self.st.append((val, mini))

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()