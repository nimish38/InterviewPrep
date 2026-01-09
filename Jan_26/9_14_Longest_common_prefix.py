class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key=lambda x: len(x))
        ref, best = strs[0], len(strs[0])
        for i in range(1, len(strs)):
            common = 0
            for j in range(min(best, len(strs[i]))):
                if ref[j] != strs[i][j]:
                    if j == 0:
                        return ""
                    else:
                        break
                else:
                    common += 1
            best = min(best, common)
        return ref[:best]


print(Solution().longestCommonPrefix(strs =["abc", "ab"]))