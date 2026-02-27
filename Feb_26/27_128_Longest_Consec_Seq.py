class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        freq, curr, best = {}, 1, 0
        for num in nums:
            freq[num] = 1
        for key in freq:
            if key - 1 not in freq:
                while key + 1 in freq:
                    curr += 1
                    key += 1
                best = max(curr, best)
                curr = 1
        return best

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))