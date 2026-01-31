class Solution(object):
    def maxSubArray(self, nums):
        n, curr, best, flag, biggest = len(nums), 0, 0, False, float('-inf')
        for i in range(n):
            if nums[i] + curr < 0:
                curr = 0
            else:
                flag = True
                curr += nums[i]
            best = max(best, curr)
            biggest = max(biggest, nums[i])
        if not flag:
            return biggest
        return max(curr, best)

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))