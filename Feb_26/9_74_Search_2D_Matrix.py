class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        def binSearchRow():
            u, d = 0, m - 1
            mid = (u + d) // 2
            row = mid
            while u <= d:
                mid = (u + d) // 2
                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] > target:
                    d = mid - 1
                else:
                    row = mid
                    u = mid + 1
            return row

        def binSearchCol(row):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        row = binSearchRow()
        return binSearchCol(row)


print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))