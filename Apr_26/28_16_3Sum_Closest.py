class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        i, j, n, res, diff = 0, 1, len(nums), -1, float('inf')
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                curr = abs(target - val)
                if curr < diff:
                    diff, res = curr, val
                if val < target:
                    j += 1
                else:
                    k -= 1
        return res

print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
