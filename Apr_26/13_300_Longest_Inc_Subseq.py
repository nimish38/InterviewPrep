class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = [[-1] * n for _ in range(n + 1)]

        def solve(ind, last):
            if ind >= n:
                return 0
            if memo[ind][last + 1] == -1:
                take, skip = -1, -1
                if last == -1 or nums[ind] > nums[last]:
                    take = 1 + solve(ind + 1, ind)
                skip = solve(ind + 1, last)
                memo[ind][last + 1] = max(take, skip)
            return memo[ind][last + 1]
        return solve(0, -1)

print(Solution().lengthOfLIS(nums = [3,5,6,2,5,4,19,5,6,7,12]))