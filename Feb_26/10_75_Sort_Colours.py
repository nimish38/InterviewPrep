class Solution(object):
    def sortColors(self, nums):
        i, k = 0, len(nums) - 1
        while nums[i] == 0:
            i += 1
        while nums[k] == 2:
            k -= 1
        j = i + 1
        while i < k and k > j > i:
            if nums[i] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            if nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
            if nums[k] == 1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
        return nums


print(Solution().sortColors(nums = [2,0,2,1,1,0]))