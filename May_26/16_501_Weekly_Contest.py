from math import isqrt

class Solution(object):
    def minArraySum(self, nums):
        present = set(nums)
        total = 0
        for x in nums:
            best = x
            for d in range(1, isqrt(x) + 1):
                if x % d == 0:
                    # First divisor
                    if d in present:
                        best = min(best, d)
                    # Paired divisor
                    other = x // d
                    if other in present:
                        best = min(best, other)
            total += best
        return total

print(Solution().minArraySum(nums = [14, 7]))