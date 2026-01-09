class Solution(object):
    def longestCommonPrefix(self, strs):
        ref, best = strs[0], len(strs[0])
        for i in range(1, len(strs)):
            for j in range(min(best, len(strs[i]))):
                if ref[j] != strs[i][j]:
                    if j == 0:
                        return ""
                    else:
                        best = min(best, j)
        return best


