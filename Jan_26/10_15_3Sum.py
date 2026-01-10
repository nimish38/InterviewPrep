class Solution(object):
    def threeSum(self, nums):
        res, n = [], len(nums)
        for i in range(n - 2):
            seen, target = {}, -nums[i]
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    res.append([nums[i], nums[seen[target - nums[j]]], nums[j]])
                    continue
                else:
                    seen[nums[j]] = j
        return res