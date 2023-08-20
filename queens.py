def print_n_queens(board, ans, row):
    if (row == len(board)):
        print(ans+'.')
        print(board)
        return
    for col in range(len(board)):
        if (board[row][col] == 0 and is_queen_safe(board, row, col) == True):
            board[row][col] = 1
            print_n_queens(board, ans+str(row)+"-"+str(col)+",", row+1)
            board[row][col] = 0


def is_queen_safe(board, row, col):
    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper row
    i = row - 1
    j = col
    while i >= 0:
        if board[i][j] == 1:
            return False
        i -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check left column
    i = row
    j = col - 1
    while j >= 0:
        if board[i][j] == 1:
            return False
        j -= 1

    return True


n = int(input("Number  of queens : "))
board = [[0]*n for _ in range(n)]

print_n_queens(board, "", 0)
