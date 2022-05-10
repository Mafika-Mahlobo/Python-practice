def play(size, bomb):
    under_grid = add_bombs(size, bomb)
    draw_grid(size, under_grid,None)
    cont = ''
    while cont != 'Q':
        hori = int(input('x: '))
        veti = int(input('Y: '))
        
        if under_grid[veti][hori] == 'B':
            lost(under_grid, size)
            break
        else:
            c = mine_count(veti, hori, under_grid)
            draw_grid(size,under_grid, c)
        while cont != 'C' and cont != 'Q':
            cont = input('type C to continue playing or Q to quit: ').upper()
            
        

def horizontal_line(length):
    for i in range(length):
        print('-----',end='')
    print()

def X_axis_numbering(number):
    for col in range(number):
        if col != number:
            print('   {}'.format(col),end='')
    print()


def add_bombs(side_size, bomb):
    import random
    board = []

    for i in range(side_size):
        board.append([])
        for j in range(side_size):
            board[i].append('')

    while bomb > 0:
        randNum = random.randint(0,side_size-1)
        randNum1 = random.randint(0,side_size-1)
        if board[randNum][randNum1] == '':
            board[randNum][randNum1] = 'B'
            bomb -= 1
            
    return board
    
	
	    	
def draw_grid(dim_size, board, coordinates):
    row_count = 0
    X_axis_numbering(dim_size)
    horizontal_line(dim_size)
    
    
    for i in board:
        if row_count < dim_size:
            print('{} '.format(row_count),end='')
            row_count += 1
        for j in i:
            if j == coordinates and j != '' and j != 'B':
                print('|%s  '%j,end='')      
            else:
                print('|   ',end='')
        print()
        
    horizontal_line(dim_size)

    
def lost(board, dim_size):
    row_num = 0
    X_axis_numbering(dim_size)
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

def mine_count(_y_axis, _x_axis, board):
    board[_y_axis][_x_axis] = 0
    for row in board:
        for col in row:
            if board[_y_axis][_x_axis] == 0:
                if col != row[0]:
                    if board[_y_axis][_x_axis-1] == 'B':
                        board[_y_axis][_x_axis] += 1
                if col != row[len(row)-1]:
                    if board[_y_axis][_x_axis+1] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[0]:
                    if board[_y_axis-1][_x_axis] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[0] and col != row[0]:
                    if board[_y_axis-1][_x_axis-1] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[0] and col != row(len(row)-1):
                    if board[_y_axis-1][_x_axis+1] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[len(row)-1]:
                    if board[_y_axis+1][_x_axis] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[len(row)-1] and col != row[0]:
                    if board[_y_axis+1][_x_axis-1] == 'B':
                        board[_y_axis][_x_axis] += 1
                if row != board[len(row)-1] and col != row[len(row)-1]:
                    if board[_y_axis+1][_x_axis+1] == 'B':
                        board[_y_axis][_x_axis] += 1
    return board[_y_axis][_x_axis]
    
    
                 
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
    play(size, bombs)
        
print(' ')
print('GOOD BYE!')
