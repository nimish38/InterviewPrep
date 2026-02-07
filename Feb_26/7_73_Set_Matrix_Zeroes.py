class Solution(object):
    def setZeroes(self, matrix):
        rowZero, colZero, m, n = False, False, len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0:
                        rowZero = True
                    if j == 0:
                        colZero = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if rowZero:
            matrix[0] = [0] * n
        if colZero:
            for _ in range(m):
                matrix[_][0] = 0
        return matrix


print(Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))