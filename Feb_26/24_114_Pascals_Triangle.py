class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        pascal, curr = [[1], [1, 1]], [1]
        for i in range(3, numRows):
            last = pascal[-1]
            for j in range(len(last) - 1):
                curr.append(last[j] + last[j + 1])
            curr.append(1)
            pascal.append(curr)
            curr = [1]
        return pascal