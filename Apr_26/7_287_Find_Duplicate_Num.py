class Solution(object):
    def findDuplicate(self, nums):
        maps = set()
        for num in nums:
            if num in maps:
                return num
            maps.add(num)
        return -1

print(Solution().findDuplicate(nums = [1,3,4,2,2]))