class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        maps, res, st = {}, [], []
        for i in range(len(nums2), -1, -1):
            if not st:
                st.append(nums2[i])
                maps[nums2[i]] = -1
            else:
                while st and st[-1] < nums2[i]:
                    st.pop()
                if st:
                    maps[nums2[i]] = st[-1]
                else:
                    maps[nums2[i]] = -1
                st.append(nums2[i])

        for num in nums1:
            res.append(maps[num])
        return res

