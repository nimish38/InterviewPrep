class StockSpanner:

    def __init__(self):
        self.st, self.cnt = [], 0

    def next(self, price: int):
        if not self.st:
            self.st.append((price, self.cnt))
            self.cnt += 1
            return 1
        while self.st and self.st[-1][0] < price:
            self.st.pop()
        last = 0
        if self.st:
            last = self.st[-1][1]
        self.st.append((price, self.cnt))
        self.cnt += 1
        return self.cnt - last - 1


obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))