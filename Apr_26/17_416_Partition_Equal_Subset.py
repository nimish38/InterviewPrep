class Solution(object):
    def canPartition(self, nums):
        n, target = len(nums), sum(nums)
        if target % 2:
            return False
        nums.sort()
        def solve(ind, curr):
            if ind == n:
                return False
            take, skip, combo = False, False, curr + nums[ind]
            if combo == ans:
                return True
            if combo < ans:
                take = solve(ind + 1, combo)
            skip = solve(ind + 1, curr)
            return take or skip
        ans = target // 2
        return solve(0, 0)

print(Solution().canPartition( nums = [2,5,12,5]))