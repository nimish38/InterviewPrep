import heapq
from collections import defaultdict


class Solution(object):
    def getSkyline(self, buildings):
        cords, res = [], []
        for l, r, h in buildings:
            cords.append((l, -h))
            cords.append((r, h))
        cords.sort()
        pq, prev, deleted = [0], 0, defaultdict(int)
        for x, ht in cords:
            if ht < 0:
                heapq.heappush(pq, ht)
                if -pq[0] > prev:
                    res.append([x, -ht])
                    prev = -ht
            else:
                deleted[ht] += 1
                while -pq[0] in deleted:
                    deleted[-pq[0]] -= 1
                    if deleted[-pq[0]] == 0:
                        del deleted[-pq[0]]
                    heapq.heappop(pq)
                if -pq[0] != prev:
                    res.append([x, -pq[0]])
                    prev = -pq[0]
        return res

print(Solution().getSkyline(buildings = [[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]))