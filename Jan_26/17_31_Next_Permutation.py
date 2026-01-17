class Solution(object):
    def nextPermutation(self, nums):
        def reverse(ind):
            i, j = ind + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i, j = len(nums) - 2, len(nums) - 1
        while j >= 0:
            while i >= 0 and nums[i] > nums[j]:
                i -= 1
            if i >= 0:
                nums[i], nums[j] = nums[j], nums[i]
                reverse(i)
                return nums
            else:
                j = j - 1
                i = j - 1

        reverse(-1)
        return nums


x = [3,2,1]
# for _ in range(12):
#     x = Solution().nextPermutation(x)
#     print(x)
print(Solution().nextPermutation(x))
