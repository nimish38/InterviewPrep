import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.nums, self.k = nums, k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) + 1 <= self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


kthLargest = KthLargest(1, [])
print(kthLargest.add(-3))
print(kthLargest.add(-2))
print(kthLargest.add(-4))
print(kthLargest.add(0))
print(kthLargest.add(4))