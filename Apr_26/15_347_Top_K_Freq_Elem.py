import heapq
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        cnt, heap = defaultdict(int), []
        for num in nums:
            cnt[num] += 1
        for num in cnt:
            if len(heap) < k:
                heapq.heappush(heap, (cnt[num], num))
            else:
                heapq.heappushpop(heap, (cnt[num], num))
        return list(map(lambda x: x[1], heap))

print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2))