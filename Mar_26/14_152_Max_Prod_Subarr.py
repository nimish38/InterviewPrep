class Solution(object):
    def maxProduct(self, nums):
        n, best = len(nums), max(nums)
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                curr = 1
                for k in nums[j: j + i]:
                    curr *= k
                    if k == 0:
                        break
                if curr > best:
                    best = curr
        return best

print(Solution().maxProduct(nums = [2,3,-2,4]))