class Solution(object):
    def majorityElement(self, nums):
        major, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                cnt += 1
            else:
                if cnt == 0:
                    major, cnt = nums[i], 1
                else:
                    cnt -= 1
        return major

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))