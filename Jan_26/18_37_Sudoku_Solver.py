from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board):
        empty = []
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    col[j].add(num)
                    row[i].add(num)
                    val = (i // 3) * 3 + (j // 3)
                    box[val].add(num)
                else:
                    empty.append((i, j))

        def solve(ind):
            if ind == len(empty):
                return True
            i, j = empty[ind]
            val = (i // 3) * 3 + (j // 3)
            for k in range(1, 10):
                if k not in row[i] and k not in col[j] and k not in box[val]:
                    board[i][j] = str(k)
                    col[j].add(k)
                    row[i].add(k)
                    box[val].add(k)        
                    if solve(ind + 1):
                        return True
                    col[j].remove(k)
                    row[i].remove(k)
                    box[val].remove(k)
                    board[i][j] = '.'
            return False
            
        solve(0)
        return board
    

print(Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
                                      ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                                      [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))