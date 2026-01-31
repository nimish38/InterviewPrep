class Solution(object):
    def maxSubArray(self, nums):
        n, curr, best = len(nums), 0, 0
        for i in range(n):
            if nums[i] + curr < 0:
                curr = 0
            else:
                curr += nums[i]
            best = max(best, curr)
        return max(curr, best)

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))