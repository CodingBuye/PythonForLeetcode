class Solution:
    def numRookCaptures(self, board):
        capture = 0
        rook_row = None
        rook_col = None

        if not board or not board[0]:
            return 0

        for row in board:
            if 'R' in row:
                rook_col = row.index('R')
                rook_row = board.index(row)
                break

        north = [board[k][rook_col] for k in range(rook_row)]
        east = board[rook_row][rook_col+1:]
        south = [board[k][rook_col] for k in range(rook_row+1, 8)]
        west = board[rook_row][:rook_col]

        for x in reversed(north):
            if x != 'p' and x != '.':
                break
            elif x == 'p':
                capture += 1
                break

        for x in east:
            if x != 'p' and x != '.':
                break
            elif x == 'p':
                capture += 1
                break

        for x in south:
            if x != 'p' and x != '.':
                break
            elif x == 'p':
                capture += 1
                break

        for x in reversed(west):
            if x != 'p' and x != '.':
                break
            elif x == 'p':
                capture += 1
                break

        return capture


if __name__ == "__main__":
    inputs = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    res = Solution().numRookCaptures(inputs)
    print(res)
