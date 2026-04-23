class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr, best = 0, 0
        for n in nums:
            if n:
                curr += 1
            else:
                if curr > best:
                    best = curr
                curr = 0
        return max(best, curr)

print(Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))