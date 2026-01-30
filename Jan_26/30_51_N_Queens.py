class Solution(object):
    def solveNQueens(self, n):
        board, ans, col, diag, anti = [[0]*n for _ in range(n)], [], set(), set(), set()
        def format_board(chess):
            res = []
            for _ in range(n):
                val = ''
                for j in range(n):
                    if chess[_][j]:
                        val += 'Q'
                    else:
                        val += '.'
                res.append(val)
            ans.append(res)

        def solve(r):
            if r >= n:
                format_board(board)
                return
            for c in range(n):
                di, an = r + c, r - c
                if c not in col and di not in diag and an not in anti:
                    col.add(c)
                    diag.add(di)
                    anti.add(an)
                    board[r][c] = 1
                    solve(r + 1)
                    col.remove(c)
                    diag.remove(di)
                    anti.remove(an)
                    board[r][c] = 0

        solve(0)
        return ans

print(Solution().solveNQueens(n = 4))