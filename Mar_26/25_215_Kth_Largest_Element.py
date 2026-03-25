import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        x = []
        for num in nums:
            heapq.heappush(x, -num)
        for _ in range(k - 1):
            heapq.heappop(x)
        return -heapq.heappop(x)

print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))
