class Solution(object):
    def subsetsWithDup(self, nums):
        n, res = len(nums), []
        def solve(ind, combo):
            if ind == n:
                x = sorted(list(combo))
                if x not in res:
                    res.append(x)
                return
            combo.append(nums[ind])
            solve(ind + 1, combo)
            combo.pop()
            solve(ind + 1, combo)
        solve(0, [])
        return res

print(Solution().subsetsWithDup([1, 2, 2]))