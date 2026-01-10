class Solution(object):
    def threeSum(self, nums):
        res, n = [], len(nums)
        for i in range(n - 2):
            seen, target = {}, -nums[i]
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    triplet = sorted([nums[i], nums[seen[target - nums[j]]], nums[j]])
                    if triplet not in res:
                        res.append(triplet)
                    continue
                else:
                    seen[nums[j]] = j
        return res


print(Solution().threeSum(nums = [2,-4,1,2,-2,2,0,2]))