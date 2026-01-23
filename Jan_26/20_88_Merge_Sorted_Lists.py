class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:m]
        nums1 += nums2
        nums1.sort()

print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))