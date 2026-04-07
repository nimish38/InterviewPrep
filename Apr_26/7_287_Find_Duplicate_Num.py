class Solution(object):
    def findDuplicate(self, nums):
        for num in nums:
            x = abs(num)
            if nums[x] < 0:
                return x
            nums[x] = - nums[x]
        return -1

print(Solution().findDuplicate(nums = [1,3,4,2,2]))