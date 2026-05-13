class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        flag = False
        for i in range(31):
            if n & 1:
                if not flag:
                    flag = True
                else:
                    return False
            n >>= 1
        return flag

print(Solution().isPowerOfTwo(n = -2147483648))