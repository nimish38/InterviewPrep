class Solution(object):
    def nextPermutation(self, nums):
        def reverse(ind):
            i, j = ind + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        idx = -1
        length = len(nums)

        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            reverse(-1)
            return nums

        reverse(idx)
        newj = -1
        for j in range(idx + 1, length):
            if nums[idx] < nums[j]:
                newj = j
                break

        nums[idx], nums[newj] = nums[newj], nums[idx]
        return nums


x = [3,2,1]
# for _ in range(12):
#     x = Solution().nextPermutation(x)
#     print(x)
print(Solution().nextPermutation(x))
