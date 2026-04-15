import heapq
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        cnt, heap = defaultdict(int), []
        for num in nums:
            cnt[num] += 1
        return sorted(cnt, key = cnt.get, reverse = True)[:k]

print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2))