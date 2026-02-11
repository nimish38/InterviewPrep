class Solution(object):
    def subsetsWithDup(self, nums):
        n, res = len(nums), []
        def solve(ind, combo):
            if ind == n:
                res.append(list(combo))
                return
            combo.append(nums[ind])
            solve(ind + 1, combo)
            combo.pop()
            solve(ind + 1, combo)
        solve(0, [])
        return res

print(Solution().subsetsWithDup([1, 2, 3]))