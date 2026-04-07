class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

print(Solution().findDuplicate(nums = [1,3,4,2,2]))