class Solution(object):
    def partition(self, s):
        n, res = len(s), []
        def solve(ind, curr):
            if ind >= n:
                res.append(curr.copy())
                return
            for i in range(ind + 1, n + 1):
                partition = s[ind: i]
                if partition == partition[::-1]:
                    curr.append(partition)
                    solve(i, curr)
                    curr.pop()
        solve(0, [])
        return res

print(Solution().partition(s = "aab"))