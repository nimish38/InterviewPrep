class StockSpanner:

    def __init__(self):
        self.st, self.cnt = [], 0

    def next(self, price: int):
        while self.st and self.st[-1][0] < price:
            self.st.pop()
        last = 0
        if self.st:
            last = self.st[-1][1]
        self.st.append((price, self.cnt))
        self.cnt += 1
        return self.cnt - last


