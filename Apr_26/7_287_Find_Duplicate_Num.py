class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1

print(Solution().findDuplicate(nums = [1,3,4,2,2]))