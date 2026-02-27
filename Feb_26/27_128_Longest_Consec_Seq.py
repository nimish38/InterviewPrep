class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums, curr, best = set(nums), 1, 0
        for key in nums:
            if key - 1 not in nums:
                while key + 1 in nums:
                    curr += 1
                    key += 1
                best = max(curr, best)
                curr = 1
        return best

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))