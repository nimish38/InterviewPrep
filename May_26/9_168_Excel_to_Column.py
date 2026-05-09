class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ''
        while columnNumber > 26:
            rem, columnNumber = columnNumber % 26, columnNumber // 26
            res = chr(64 + rem) + res
        return chr(64 + columnNumber) + res

print(Solution().convertToTitle(703))