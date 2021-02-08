board = [
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 2, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 6, 1],
    [4, 7, 0, 0, 2, 0, 0, 0, 0],
    [5, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 9, 1, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 2, 0, 0],
    [3, 0, 8, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 4, 0]
]


def solve(board):
    position = find_empty(board)
    if not position:
        return True
    else:
        row, col = position
    for i in range(1, len(board) + 1):
        if isValid(board, i, position):
            board[row][col] = i
            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], " ", end="")
        print()


printBoard(board)
print("\n")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


def isValid(board, value, position):
    box_x = position[0] - (position[0] % 3)
    box_y = position[1] - (position[1] % 3)


    # Check Box
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    # Check Row
    for i in range(len(board)):
        if board[position[0]][i] == value and position[1] != i:
            return False

    # Check Column
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] != i:
            return False
    return True

#solve(board)
printBoard(board)
