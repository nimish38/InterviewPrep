class Solution(object):
    def reversePairs(self, nums):
        self.res, n = 0, len(nums)

        def divide(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left, right = divide(arr[:mid]), divide(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            l1, l2, i, j, arr = len(left), len(right), 0, 0, []
            while i < l1 and j < l2:
                if left[i] > 2 * right[j]:
                    j += 1
                else:
                    self.res += j
                    i += 1
            if i < l1:
                self.res += (l1 - i) * j
            i, j = 0, 0
            while i < l1 and j < l2:
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            if i < l1:
                arr.extend(left[i:])
            if j < l2:
                arr.extend(right[j:])
            return arr

        divide(nums)
        return self.res

print(Solution().reversePairs(nums = [1,3,2,3,1]))