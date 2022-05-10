
# Implement your Minesweeper Solution Below:

def play(dim_size, num_bombs):
    board = add_bombs(dim_size, num_bombs)
    draw_board(dim_size, board)
    continue_play = ''
    while continue_play != 'Q':
        print(' ')
        print('select block')
        _x_axis = int(input('x-axis: '))
        _y_axis = int(input('Y-yaxis: '))
        if board[_y_axis][_x_axis] == 'B':
            lost(board, dim_size)
            break
        else:
            board[_y_axis][_x_axis] = 0
            draw_board(dim_size,board)
            continue_play = ''
        while continue_play != 'C' and continue_play != 'Q':
            continue_play = input('type C to continue playing or Q to quit: ').upper()

def draw_board(dim_size, board):
    row_count = 0

    #numbering the x-axis
    X_axis_numbering(dim_size)
    
    #drawing horizontal line before drawing board
    horizontal_line(dim_size)

    #iteratre through board
    for i in board:

        #numbering y-axis
        if row_count < dim_size:
            print('{} '.format(row_count),end='')
            row_count += 1
        for j in i:
            if j == 0:
                #showing user selected block if theres no bombs
                print('|%s  '%j,end='')
            else:
                #hiding uselected blocks
                print('|   ',end='')
        print()
        
    horizontal_line(dim_size)

#this function creates board and add bombs 
def add_bombs(dim_size, bombs):
    import random
    board = []

    #creating board with empty blocks
    for i in range(dim_size):
        board.append([])
        for j in range(dim_size):
            board[i].append('')

    #randomly adding bombs to the created board
    while bombs > 0:
        randNum1 = random.randint(0,dim_size-1)
        randNum2 = random.randint(0,dim_size-1)
        if board[randNum1][randNum2] == '':
            board[randNum1][randNum2] = 'B'
            bombs -= 1
            
    #return board to play() function    
    return board

def lost(board, dim_size):
    row_num = 0
    
    #numbering the x-axis
    X_axis_numbering(dim_size)
    
    #drawing horizontal line before drawing board
    horizontal_line(dim_size)
    for rows in board:
        if row_num < dim_size:
            print('%s '%row_num,end='')
            row_num += 1
        for blocks in rows:
            print('|{}  '.format(blocks),end='')
        print()
    horizontal_line(dim_size)
    
    print(' ')
    print('you loose!')

#this function draws a horizontal line using board dimention size
def horizontal_line(length):
    for i in range(length):
        print('-----',end='')
    print()

#this function add number on top of the board using its dimention size
def X_axis_numbering(number):
    for col in range(number):
        if col != number:
            print('   {}'.format(col),end='')
    print()

#def adjacent_mine_count(_y_axis, _x_axis):
    #code to check adjacent mines


#this is the program entry point
user_answer = input('Welcome to minesweper, type "Y" or any key to quit: ').upper()

if user_answer == 'Y':
    size = int(input('enter board size (one side of the borad): '))
    bombs = int(input('enter number of bombes: '))
    if bombs > size or bombs == 0:
        while bombs > size or bombs == 0:
            print(' ')
            print('> bombs must be less than the board size!')
            print('> you must enter atleast 1 bomb!')
            bombs = int(input('enter number of bombes: '))
    #call play fnction to start game
    play(size, bombs)
        
print(' ')
print('GOOD BYE!')
    
