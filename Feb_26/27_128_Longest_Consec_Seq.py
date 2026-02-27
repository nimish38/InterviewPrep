class Solution(object):
    def longestConsecutive(self, nums):
        nums = list(set(nums))
        nums.sort()
        curr, best = 1, 0
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                curr += 1
            else:
                best = max(best, curr)
                curr = 1
        return max(best, curr)

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))