class Solution(object):
    def maxProduct(self, nums):
        n, best, pre, suf = len(nums), float('-inf'), 1, 1
        for i in range(n):
            pre *= nums[i]
            suf *= nums[n - i - 1]
            best = max(best, pre, suf)
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
        return best

print(Solution().maxProduct(nums = [2,3,-2,4]))