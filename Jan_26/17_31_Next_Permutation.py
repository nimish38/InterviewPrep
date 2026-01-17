class Solution(object):
    def nextPermutation(self, nums):
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] > nums[j]:
            i -= 1
        if i < 0:
            return nums[::-1]
        left = nums[j]
        while i < len(nums):
            temp = nums[i]
            nums[i], left = left, temp
            i += 1
        return nums

