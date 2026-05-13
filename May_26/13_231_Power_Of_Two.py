class Solution(object):
    def isPowerOfTwo(self, n):
        flag = False
        for i in range(32):
            if n & 1:
                if not flag:
                    flag = True
                else:
                    return False
            n >>= 1
        return flag

print(Solution().isPowerOfTwo(n = 1024))