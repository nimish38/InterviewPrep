class Solution(object):
    def getPermutation(self, n, k):
        arr, fact, res = [], 1, ""
        for i in range(1, n):
            arr.append(i)
            fact *= i
        arr.append(n)
        k -= 1
        while True:
            num = arr[k // fact]
            arr.remove(num)
            res += str(num)
            if len(arr) == 0:
                return res
            k %= fact
            fact //= len(arr)

print(Solution().getPermutation(n = 4, k = 9))