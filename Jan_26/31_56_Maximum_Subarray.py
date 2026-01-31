class Solution(object):
    def maxSubArray(self, nums):
        n, curr, best = len(nums), float('-inf'), float('-inf')
        for i in range(n):
            if nums[i] + curr > nums[i]:
                curr += nums[i]
            else:
                curr = nums[i]
            if curr > best:
                best = curr
        return best

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))