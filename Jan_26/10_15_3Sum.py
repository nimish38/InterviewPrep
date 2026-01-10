class Solution(object):
    def threeSum(self, nums):
        res, n = [], len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen, target = {}, -nums[i]
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    res.append([nums[i], nums[seen[target - nums[j]]], nums[j]])
                    continue
                else:
                    seen[nums[j]] = j
        return res


print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))