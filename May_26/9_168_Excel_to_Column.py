class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            rem, columnNumber = columnNumber % 26, columnNumber // 26
            res = chr(65 + rem) + res
        return res

print(Solution().convertToTitle(701))