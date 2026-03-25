import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums)

print(Solution().findKthLargest())
