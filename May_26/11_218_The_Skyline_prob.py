import heapq


class Solution(object):
    def getSkyline(self, buildings):
        cords, res = [], []
        for l, r, h in buildings:
            cords.append((l, -h))
            cords.append((r, h))
        cords.sort()
        pq, prev = [0], 0
        for x, ht in cords:
            if ht < 0:
                heapq.heappush(pq, ht)
                if -pq[0] > prev:
                    res.append([x, -ht])
                    prev = -ht
            else:
                pq.remove(-ht)
                heapq.heapify(pq)
                if -pq[0] != prev:
                    res.append([x, -pq[0]])
                    prev = -pq[0]
        return res

