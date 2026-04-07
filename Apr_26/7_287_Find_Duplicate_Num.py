class Solution(object):
    def findDuplicate(self, nums):
        seen = set(nums)
        return (sum(nums) - sum(seen)) / (len(nums) - len(seen))

print(Solution().findDuplicate(nums = [1,3,4,2,2]))