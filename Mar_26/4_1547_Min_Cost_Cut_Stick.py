class Solution(object):
    def minCost(self, n, cuts):
        cuts.extend([0, n])
        cuts.sort()
        def solve(arr):
            if len(arr) <= 2:
                return 0
            val = float('inf')
            for i in range(1, len(arr) - 1):
                curr = solve(arr[: i + 1]) + solve(arr[i:]) + (arr[-1] - arr[0])
                val = min(val, curr)
            return val
        return n + solve(cuts)


print(Solution().minCost(n = 7, cuts = [1,3,4,5]))