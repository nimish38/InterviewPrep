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
                        amt += r - l
                        stick.add((l, cut))
                        stick.add((cut, r))
                        solve(stick, curr, amt)
                        stick.add((l, r))
                        curr.add(cut)
                        amt -= r - l
                        stick.remove((l, cut))
                        stick.remove((cut, r))
        solve({(0, n)}, set(cuts), 0)
        return self.cost

print(Solution().minCost(n = 9, cuts = [5,6,1,4,2]))