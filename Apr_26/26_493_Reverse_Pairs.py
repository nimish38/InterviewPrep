class Solution(object):
    def reversePairs(self, nums):
        res, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    res += 1
        return res

print(Solution().reversePairs(nums = [2,4,3,5,1]))