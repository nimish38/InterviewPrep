from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        target, maps, res = len(nums) // 3, defaultdict(int), []
        for num in nums:
            maps[num] += 1
        for key in maps:
            if maps[key] > target:
                res.append(key)
        return res