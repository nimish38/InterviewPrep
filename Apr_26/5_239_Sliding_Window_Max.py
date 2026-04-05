class Solution(object):
    def maxSlidingWindow(self, nums, k):
        heap, res = nums[: k], [max(nums[: k])]
        for i in range(k, len(nums)):
            heap.pop(0)
            heap.append(nums[i])
            res.append(max(heap))
        return res

print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))