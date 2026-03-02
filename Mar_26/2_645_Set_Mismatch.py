class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return None

print(Solution().findErrorNums(nums = [1,2,2,4]))
