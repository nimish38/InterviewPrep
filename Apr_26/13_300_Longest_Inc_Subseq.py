class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        def solve(ind, curr):
            if ind >= n:
                return len(curr)
            take, skip = -1, -1
            if not curr:
                curr.append(nums[ind])
                take = solve(ind + 1, curr)
                curr.pop()
            else:
                if nums[ind] > curr[-1]:
                    curr.append(nums[ind])
                    take = solve(ind + 1, curr)
                    curr.pop()
            skip = solve(ind + 1, curr)
            return max(take, skip)
        return solve(0, [])

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))