class Solution(object):
    def maximizeXor(self, nums, queries):
        res, curr = [], -1
        nums.sort()
        for x, m in queries:
            curr, i = -1, 0
            while i < len(nums) and nums[i] <= m:
                curr = max(curr, x ^ nums[i])
                i += 1
            res.append(curr)
        return res

print(Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))

