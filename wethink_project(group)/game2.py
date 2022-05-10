import random

# declaration of lists and variables
board = []
mines = []
board_row = 0
adj = 0
wrong = 0

# start board-size loop
while True:
    board_row = int(input('How many rows? (4 minimum): '))

    if board_row < 4:
        print('That is too small, (4 is minimum)!')
    else:
        break
#
if board_row >= 8:
    for i in range(15):
        mines.append([random.randint(0, board_row - 1), random.randint(0, board_row - 1)])
elif board_row >= 5:
    for i in range(10):
        mines.append([random.randint(0, board_row - 1), random.randint(0, board_row - 1)])

for i in range(board_row):
    board.append(['X'] * board_row)


def draw_board(board):
    for j in board:
        print('  '.join(j))


def check_ans():
    if row >= board_row or col >= board_row:
        print('That number is too high. The order goes 0 to ', board_row - 1)
        wrong = 1
    else:
        wrong = 0


def adjacent_mines(r, c, adj):
    

    if [r + 1, c] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1
    if [r + 1, c + 1] in mines:
        adj += 1

    return adj


draw_board(board)

while True:
    print('Input where you want to mine')
    row = int(input('Row: '))
    col = int(input('Column: '))

    check_ans()

    if wrong != 1:
        if [row, col] in mines:
            break
        else:
            board[row][col] = str(adjacent_mines(row, col, 0))

    # draw board if it did not hit mine
    draw_board(board)

print('Sorry but you have blown up !')
