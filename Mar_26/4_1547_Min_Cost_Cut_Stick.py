class Solution(object):
    def minCost(self, n, cuts):
        cuts.extend([0, n])
        cuts.sort()
        l = len(cuts) + 1
        memo = [[-1] * (l) for _ in range(l)]
        def solve(l, r):
            if r - l < 2:
                return 0
            if memo[l][r] == -1:
                val = float('inf')
                for i in range(l + 1, r):
                    curr = solve(l, i) + solve(i, r) + (cuts[r] - cuts[l])
                    val = min(val, curr)
                memo[l][r] = val
            return memo[l][r]
        return solve(0, len(cuts) - 1)

print(Solution().minCost(n = 9, cuts = [5,6,1,4,2]))