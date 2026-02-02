class Solution(object):
    def getPermutation(self, n, k):
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        def permute():
            def rev(x, y):
                while x < y:
                    arr[x], arr[y] = arr[y], arr[x]
                    x += 1
                    y -= 1

            j = n - 1
            while j > 0:
                for k in range(j - 1, -1, -1):
                    if arr[j] > arr[k]:
                        arr[k], arr[j] = arr[j], arr[k]
                        rev(k + 1, j)
                        return
                j -= 1
            rev(j, n - 1)

        for i in range(k):
            permute()
        return "".join(map(str, arr))


print(Solution().getPermutation(n = 3, k = 3))