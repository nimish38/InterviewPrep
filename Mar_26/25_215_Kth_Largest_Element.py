class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[len(nums) - k]
