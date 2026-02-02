import math
class Solution(object):
    def getPermutation(self, n, k):
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        def rev(x, y):
            while x < y:
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1

        def permute():
            j = n - 1
            while j > 0 and arr[j] < arr[j - 1]:
                j -= 1
            rev(j, n - 1)
            x = j
            for x in range(j, n):
                if arr[x] > arr[j - 1]:
                    break
            arr[j - 1], arr[x] = arr[x], arr[j - 1]


        if k == math.factorial(n):
            rev(0, n - 1)
            return "".join(map(str, arr))
        for i in range(k - 1):
            permute()
        return "".join(map(str, arr))


print(Solution().getPermutation(n = 4, k = 9))