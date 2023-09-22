import random

# Initialize the game board
size = 4
board = [[0 for _ in range(size)] for _ in range(size)]

# Function to print the board


def print_board():
    for row in board:
        print(' '.join(map(str, row)))
    print()

# Function to add a new 2 or 4 to the board


def add_tile():
    empty_cells = [(i, j) for i in range(size)
                   for j in range(size) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

# Function to move the tiles in a row or column


def move_line(line):
    line = [tile for tile in line if tile != 0]
    merged = [False] * len(line)

    for i in range(1, len(line)):
        if line[i] == line[i - 1] and not merged[i - 1]:
            line[i - 1] *= 2
            line[i] = 0
            merged[i - 1] = True

    line = [tile for tile in line if tile != 0]
    line += [0] * (len(board) - len(line))

    return line

# Function to transpose the board (switch rows and columns)


def transpose_board():
    global board
    board = [[board[j][i] for j in range(size)] for i in range(size)]


# Initialize the game
add_tile()
add_tile()

while True:
    print_board()
    move = input("Enter move (w/a/s/d): ").lower()

    if move == 'w':  # Move up
        for i in range(size):
            board_column = [board[j][i] for j in range(size)]
            board_column = move_line(board_column)
            for j in range(size):
                board[j][i] = board_column[j]

    elif move == 'a':  # Move left
        for i in range(size):
            board[i] = move_line(board[i])

    elif move == 's':  # Move down
        for i in range(size):
            board_column = [board[j][i] for j in range(size)]
            board_column.reverse()
            board_column = move_line(board_column)
            board_column.reverse()
            for j in range(size):
                board[j][i] = board_column[j]

    elif move == 'd':  # Move right
        for i in range(size):
            board[i].reverse()
            board[i] = move_line(board[i])
            board[i].reverse()

    else:
        print("Invalid move! Use 'w', 'a', 's', or 'd'.")

    add_tile()
