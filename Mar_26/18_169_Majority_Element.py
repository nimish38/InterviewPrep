from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        maps, n = defaultdict(int), len(nums)
        for num in nums:
            maps[num] += 1
        for key in maps:
            if maps[key] > n // 2:
                return key
        return -1

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))