class Solution(object):
    def minCost(self, n, cuts):
        self.cost = float('inf')
        def solve(stick, curr, amt):
            if len(curr) == 0:
                self.cost = min(self.cost, amt)
                return
            for cut in curr:
                for l,r in stick:
                    if l < cut < r:
                        stick.remove((l, r))
                        curr.remove(cut)
                        amt += l - r
                        stick.add((l, cut))
                        stick.add((cut, l))
                        solve(stick, curr, amt)
                        stick.add((l, r))
                        curr.add(cut)
                        amt -= l - r
                        stick.remove((l, cut))
                        stick.remove((cut, l))
        solve({(0, n)}, set(cuts), 0)
        return self.cost