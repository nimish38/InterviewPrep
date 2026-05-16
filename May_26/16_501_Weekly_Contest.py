class Solution(object):
    def concatWithReverse(self, nums):
        return nums + nums[::-1]

print(Solution().concatWithReverse([1,2,3]))