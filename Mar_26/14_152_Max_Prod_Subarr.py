class Solution(object):
    def maxProduct(self, nums):
        n, best = len(nums), float('-inf')
        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                if nums[j] == 0:
                    break
                if curr > best:
                    best = curr
        return best

print(Solution().maxProduct(nums = [2,3,-2,4]))