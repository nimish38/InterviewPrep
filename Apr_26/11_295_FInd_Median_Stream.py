import heapq


class MedianFinder(object):

    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num):
        heapq.heappush(self.maxheap, -num)
        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return (self.minheap[0] - self.maxheap[0]) // 2
        return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()