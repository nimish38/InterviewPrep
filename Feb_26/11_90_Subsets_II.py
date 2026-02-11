class Solution(object):
    def subsetsWithDup(self, nums):
        n, res = len(nums), []
        nums.sort()
        def solve(ind, combo):
            if ind == n:
                res.append(list(combo))
                return
            combo.append(nums[ind])
            solve(ind + 1, combo)
            combo.pop()
            ind += 1
            while ind < n and nums[ind] == nums[ind - 1]:
                ind += 1
            solve(ind, combo)
        solve(0, [])
        return res

print(Solution().subsetsWithDup([1, 2, 2]))