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


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
