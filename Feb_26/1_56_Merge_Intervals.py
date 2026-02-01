class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        currStart, currEnd = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            if currEnd >= newStart:
                currEnd = newEnd
            else:
                res.append([currStart, currEnd])
                currStart, currEnd = newStart, newEnd
        res.append([currStart, currEnd])
        return res