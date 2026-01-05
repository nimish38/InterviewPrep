class Solution(object):
    def shuffle(self, nums, n):
        n, even, odd = len(nums) // 2, (len(nums) // 2) - 1, 0
        right = nums[n:].copy()

        for i in range(2 * (n - 1), -1, -2):
            nums[i] = nums[even]
            even -= 1

        for i in range(1, 2 * n, 2):
            nums[i] = right[odd]
            odd += 1

        return nums


print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))

