class Solution(object):
    def longestCommonPrefix(self, strs):
        ref = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(ref):
                ref = ref[:-1]
            if ref == "":
                return ref
        return ref


print(Solution().longestCommonPrefix(strs =["abc", "ab"]))