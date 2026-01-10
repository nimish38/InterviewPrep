class Solution(object):
    def threeSum(self, nums):
        res, n = [], len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target, j, k = -nums[i], i + 1, n -1
            while j < k:
                value = nums[j] + nums[k]
                if value == target:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif value > target:
                    k -= 1
                else:
                    j += 1
        return res

print(Solution().threeSum(nums = [-4,2,2,1,3]))