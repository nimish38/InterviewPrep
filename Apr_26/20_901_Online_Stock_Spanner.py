class StockSpanner:

    def __init__(self):
        self.st, self.cnt = [], 0

    def next(self, price: int):
        while self.st and self.st[-1][0] <= price:
            self.st.pop()
        last = -1
        if self.st:
            last = self.st[-1][1]
        self.st.append((price, self.cnt))
        self.cnt += 1
        return self.cnt - last - 1


obj = StockSpanner()
print(obj.next(31))
print(obj.next(41))
print(obj.next(48))
print(obj.next(59))
print(obj.next(79))
# print(obj.next(75))
# print(obj.next(85))