class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq, ans, i, j = {}, 0, 0, 0
        while j < len(s):
            if s[j] not in freq or freq[s[j]] == 0:
                freq[s[j]] = 1
                ans = max(ans, j - i + 1)
                j += 1
            else:
                while freq[s[j]] == 1:
                    freq[s[i]] -= 1
                    i += 1
        return ans


print(Solution().lengthOfLongestSubstring(s = "pwwkew"))