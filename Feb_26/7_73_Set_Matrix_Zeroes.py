class Solution(object):
    def setZeroes(self, matrix):
        rowZero, colZero, n = False, False, len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0:
                        rowZero = True
                    if j == 0:
                        colZero = True
        for i in range(1, n):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if rowZero:
            matrix[0] = [0] * n
        if colZero:
            for _ in range(n):
                matrix[_][0] = 0
        return matrix