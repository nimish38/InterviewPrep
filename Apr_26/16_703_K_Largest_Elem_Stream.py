import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.nums, self.k = nums, k

    def add(self, val):
        if len(self.nums) + 1 < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]