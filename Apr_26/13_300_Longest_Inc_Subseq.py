class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = [[-1] * n for _ in range(n + 1)]

        def solve(ind, last, ans):
            if ind >= n:
                return ans
            if memo[ind][last + 1] == -1:
                take, skip = -1, -1
                if last == -1:
                    take = solve(ind + 1, ind, ans + 1)
                else:
                    if nums[ind] > nums[last]:
                        take = solve(ind + 1, ind, ans + 1)
                skip = solve(ind + 1, last, ans)
                memo[ind][last + 1] = max(take, skip)
            return memo[ind][last + 1]
        return solve(0, -1, 0)

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))