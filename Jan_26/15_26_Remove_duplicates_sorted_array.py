class Solution(object):
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        return len(nums), nums

print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
