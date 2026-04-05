from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deq, res = deque(), []
        for i in range(len(nums)):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res


print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))