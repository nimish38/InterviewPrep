class Solution(object):
    def findErrorNums(self, nums):
        vals, dup, mis = {}, -1, -1
        for num in nums:
            if num in vals:
                dup = num
            vals[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in vals:
                return [dup, i]
        return None

print(Solution().findErrorNums(nums = [1,2,2,4]))
