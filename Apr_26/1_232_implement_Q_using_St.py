class MyQueue(object):

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        x = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return x

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        x = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return x

    def empty(self):
        return len(self.s1) == 0
