class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))