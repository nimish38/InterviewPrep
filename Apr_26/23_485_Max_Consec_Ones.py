class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr, best = 0, 0
        for n in nums:
            if n:
                curr += 1
            else:
                best, curr = max(best, curr), 0
        return max(best, curr)