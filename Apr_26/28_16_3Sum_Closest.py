class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        i, j, res, diff = 0, 1, -1, float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = nums[i] + nums[j] + nums[k]
                    curr = abs(target - val)
                    if curr < diff:
                        diff, res = curr, val
        return res

print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
