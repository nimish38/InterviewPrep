from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board):
        row, col, filled = defaultdict(set), defaultdict(set), 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    filled += 1
                    col[j].add(board[i][j])
                    row[i].add(board[i][j])
        self.empty = 81 - filled

        def solve():
            if self.empty == 0:
                return True
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if chr(k) not in row[i] and chr(k) not in col[j]:
                                board[i][j] = chr(k)
                                col[j].add(board[i][j])
                                row[i].add(board[i][j])
                                self.empty -= 1
                                if solve():
                                    return True
                                col[j].remove(board[i][j])
                                row[i].remove(board[i][j])
                                self.empty += 1
                        return False
            return False
            
        solve()
        return board
    

print(Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
                                      ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                                      [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))