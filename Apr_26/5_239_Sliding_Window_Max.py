from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deq, res = deque(), []
        for i in range(k):
            while deq and nums[deq[0]] < nums[i]:
                deq.popleft()
            deq.append(i)
        for i in range(k, len(nums)):
            while deq[0] < i - k:
                deq.popleft()
            res.append(nums[deq[0]])
            while deq and nums[deq[0]] < nums[i]:
                deq.popleft()
            deq.append(i)
        while deq[0] < len(nums) - k:
            deq.popleft()
        res.append(nums[deq[0]])
        return res


print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))