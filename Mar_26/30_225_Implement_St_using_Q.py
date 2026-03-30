class MyStack(object):
    def __init__(self):
        self.q1, self.cnt = [], 0

    def push(self, x):
        self.q1.append((x, self.cnt))
        self.cnt += 1

    def pop(self):
        if len(self.q1) == 1:
            return self.q1.pop(0)
        top, last = self.q1.pop(0), -1
        self.q1.append(top)
        while True:
            last = self.q1.pop(0)
            if self.q1[0][1] != top[1]:
                self.q1.append(last)
            else:
                break
        return last[0]

    def top(self):
        if len(self.q1) == 1:
            return self.q1[0][0]
        top, last = self.q1.pop(0), -1
        self.q1.append(top)
        while True:
            last = self.q1.pop(0)
            self.q1.append(last)
            if self.q1[0][1] == top[1]:
                break
        return last[0]

    def empty(self):
        return len(self.q1) == 0