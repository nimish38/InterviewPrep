class Solution(object):
    def compareVersion(self, version1, version2):
        version1, version2, i = list(map(int, version1.split('.'))),  list(map(int, version2.split('.'))), 0
        for i in range(min(len(version1), len(version2))):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1
        if i < len(version1):
            for j in range(i, len(version1)):
                if version1[j] > 0:
                    return 1
        if i < len(version2):
            for j in range(i, len(version2)):
                if version2[j] > 0:
                    return -1
        return 0



print(Solution().compareVersion(version1 = "1.2", version2 = "1.10"))
