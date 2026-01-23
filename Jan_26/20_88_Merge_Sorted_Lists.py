class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m, n, j = m - 1, n - 1, m + n - 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[j] = nums2[n]
                n -= 1
            else:
                nums1[j] = nums1[m]
                m -= 1
            j -= 1
        while n >= 0:
            nums1[j] = nums2[n]
            j -= 1
            n -= 1
        return nums1

print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))