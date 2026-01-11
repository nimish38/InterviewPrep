class Solution(object):
    def fourSum(self, nums, target):
        n, res, i = len(nums), [], 0
        nums.sort()
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                k, l = j + 1, n - 1
                while k < l:
                    value = nums[i] + nums[j] + nums[k] + nums[l]
                    if value == target:
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                    elif value < target:
                        k += 1
                    else:
                        l -= 1
                while j < n - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < n - 3  and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res


print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))