class Solution(object):
    def compareVersion(self, version1, version2):
        i, j, l1, l2 = 0, 0, len(version1), len(version2)
        while i < l1 and j < l2:
            num1, num2 = '', ''
            while i < l1 and version1[i] != '.':
                num1 += version1[i]
                i += 1
            while j < l2 and version2[j] != '.':
                num2 += version2[j]
                j += 1
            i += 1
            j += 1
            num1, num2 = int(num1), int(num2)
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        while i < l1:
            num1 = ''
            while i < l1 and version1[i] != '.':
                num1 += version1[i]
                i += 1
            if int(num1) > 0:
                return 1
            i += 1
        while j < l2:
            num2 = ''
            while j < l2 and version2[j] != '.':
                num2 += version2[j]
                j += 1
            if int(num2) > 0:
                return -1
            j += 1
        return 0


print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0.0"))
