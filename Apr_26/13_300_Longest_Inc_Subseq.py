class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        memo = [[-1] *( n + 1 ) for _ in range(n + 1)]

        def solve(ind, prev):
            if ind >= n:
                return 0
            if memo[ind][prev] == -1:
                take, skip = 0, 0
                if prev == -1 or nums[ind] > nums[prev]:
                    take = 1 + solve(ind + 1, ind)
                skip = solve(ind + 1, prev)
                memo[ind][prev] = max(take, skip)
            return memo[ind][prev]

        return solve(0, -1)

print(Solution().lengthOfLIS(nums = [3,5,6,2,5,4,19,5,6,7,12]))