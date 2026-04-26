class Solution:
    def reversePairs(self, nums):
        def sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, c1 = sort(arr[:mid])
            right, c2 = sort(arr[mid:])
            count = c1 + c2
            j = 0
            for i in left:
                while j < len(right) and i > 2 * right[j]:
                    j += 1
                count += j
            return sorted(left + right), count

        return sort(nums)[1]

print(Solution().reversePairs(nums = [1,3,2,3,1]))