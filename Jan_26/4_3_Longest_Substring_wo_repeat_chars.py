class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq, ans, i, j = {}, 0, 0, 0
        while j < len(s):
            if s[j] not in freq or freq[s[j]][0] == 0:
                freq[s[j]] = [1, j]
                ans = max(ans, j - i + 1)
                j += 1
            else:
                i = max(i, freq[s[j]][1] + 1)
                freq[s[j]][0] = 0
        return ans


print(Solution().lengthOfLongestSubstring(s = "abba"))