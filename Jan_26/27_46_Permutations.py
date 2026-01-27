class Solution(object):
    def permute(self, nums):
        res, n = [], len(nums)
        def solve(ind):
            if ind >= n:
                return
            for i in range(ind, n - 1):
                for j in range(i + 1, n):
                    nums[i], nums[j] = nums[j], nums[i]
                    res.append(nums.copy())
                    solve(ind + 1)
                    nums[i], nums[j] = nums[j], nums[i]
        solve(0)
        return res

print(Solution().permute(nums = [1,2,3]))