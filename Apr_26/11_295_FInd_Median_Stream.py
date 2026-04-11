import heapq
class MedianFinder(object):
    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num):
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
            if len(self.maxheap) - len(self.minheap) > 1:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        else:
            heapq.heappush(self.minheap, num)
            if len(self.minheap) - len(self.maxheap) > 0:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        return -self.maxheap[0]


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())