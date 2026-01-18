from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board):
        row, col, box, self.empty = defaultdict(set), defaultdict(set), defaultdict(set), 81
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col[j].add(board[i][j])
                    row[i].add(board[i][j])
                    val = str(i // 3) + 'R' + str(j // 3) + 'C'
                    box[val].add(board[i][j])
                    self.empty -= 1

        def solve():
            if self.empty == 0:
                return True
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            x = str(k)
                            val = str(i // 3) + 'R' + str(j // 3) + 'C'
                            if x not in row[i] and x not in col[j] and x not in box[val]:
                                board[i][j] = x
                                col[j].add(board[i][j])
                                row[i].add(board[i][j])
                                box[val].add(board[i][j])        
                                self.empty -= 1
                                if solve():
                                    return True
                                col[j].remove(board[i][j])
                                row[i].remove(board[i][j])
                                box[val].remove(board[i][j])
                                board[i][j] = '.'
                                self.empty += 1
                        return False
            return False
            
        solve()
        return board
    

print(Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
                                      ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                                      [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))