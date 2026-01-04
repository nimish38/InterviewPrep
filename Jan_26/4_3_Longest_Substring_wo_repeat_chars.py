class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq, ans, i, j = {}, 0, 0, 0
        while j < len(s):
            while s[j] in freq:
                del freq[s[i]]
                i += 1
            freq[s[j]] = 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


print(Solution().lengthOfLongestSubstring(s = "pwwkew"))