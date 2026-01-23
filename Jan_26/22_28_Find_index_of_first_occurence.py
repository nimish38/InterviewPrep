class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def match(i):
            for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        return 0
            return 1

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and match(i):
                return i
        return -1
    
print(Solution().strStr(haystack = "sacdbutsadcd", needle = "sad"))