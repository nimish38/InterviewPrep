class Solution(object):
    def canPartition(self, nums):
        n, target = len(nums), sum(nums)
        if target % 2:
            return False
        ans = target // 2
        memo = [[-1] * (ans + 1) for _ in range(n)]
        def solve(ind, curr):
            if ind == n:
                return False
            if memo[ind][curr] == -1:
                take, skip, combo = False, False, curr + nums[ind]
                if combo == ans:
                    memo[ind][curr] = True
                else:
                    if combo < ans:
                        take = solve(ind + 1, combo)
                        skip = solve(ind + 1, curr)
                        memo[ind][curr] =  take or skip
            return memo[ind][curr]
        return solve(0, 0)

print(Solution().canPartition( nums = [2,5,12,5]))