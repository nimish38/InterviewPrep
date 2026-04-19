class Solution(object):
    def findMaximumXOR(self, nums):
        res = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = max(res, nums[i] ^ nums[j])
        return res

print(Solution().findMaximumXOR(nums = [3,10,5,25,2,8]))