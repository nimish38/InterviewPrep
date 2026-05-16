class Solution(object):
    def minArraySum(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 1):
            j = len(nums) - 1
            while i < j and nums[i] > nums[j]:
                if nums[i] % nums[j] == 0:
                    nums[i] = nums[j]
                    break
                j -= 1
        return sum(nums)

print(Solution().minArraySum(nums = [4,2,8,3]))