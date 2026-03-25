import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        arr = []
        for num in nums:
            heapq.heappush(arr, num)
            if len(arr) > k:
                heapq.heappop(arr)
        return heapq.heappop(arr)

print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))
