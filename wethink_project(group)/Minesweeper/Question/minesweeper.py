try:
    def play(dim_size, num_bombs):
        board = add_bombs(dim_size, num_bombs)
        draw_board(dim_size, board)
        continue_play = ''
        while continue_play != 'Q':
            if check_win(board) == False:
                print(' ')
                print('select block')
                _x_axis = int(input('x-axis: '))
                _y_axis = int(input('Y-axis: '))
                if _x_axis < dim_size and _y_axis < dim_size:
                    if board[_y_axis][_x_axis] == 'B':
                        lost(board, dim_size)
                        continue_play = 'Q'
                    else:
                        
                            board[_y_axis][_x_axis] = bomb_count(board,_y_axis,_x_axis)
                            draw_board(dim_size,board)
                            continue_play = ''
                            while continue_play != 'C' and continue_play != 'Q':
                                continue_play = input('type C to continue playing or Q to quit: ').upper()        
                else:
                    print('coordinates are not on the boards')
            else:
                win(board,dim_size)
                continue_play = 'Q'
                


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
                print('{}'.format(row_count),end='')
                row_count += 1
                for j in i:
                    if j != '' and j != 'B':
                        #showing user selected block if theres no bombs
                        print('|%s   '%j,end='')
                    else:
                        #hiding uselected blocks
                        print('|    ',end='')
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

        row_count = 0

        #numbering the x-axis
        X_axis_numbering(dim_size)
    
        #drawing horizontal line before drawing board
        horizontal_line(dim_size)

        #iteratre through board
        for i in board:
            #numbering y-axis
            if row_count < dim_size:
                print('{}'.format(row_count),end='')
                row_count += 1
                for j in i:
                    #showing user selected block if theres no bombs
                    if j != '':
                        print('|%s  '%j,end='')
                    else:
                        print('|   ',end='')   
                print()
        
        horizontal_line(dim_size)
    
        print(' ')
        print('Sorry but you have blown up !')

    def check_win(board)->bool:
        win = True
        for row in board:
            for column in row:
                if column == '':
                    win = False
        return win

    def win(board, dim_size):
        row_count = 0

        #numbering the x-axis
        X_axis_numbering(dim_size)
    
        #drawing horizontal line before drawing board
        horizontal_line(dim_size)

        #iteratre through board
        for i in board:
            #numbering y-axis
            if row_count < dim_size:
                print('{}'.format(row_count),end='')
                row_count += 1
                for j in i:
                    #showing user selected block if theres no bombs
                    if j != '':
                        print('|%s  '%j,end='')
                    else:
                        print('|   ',end='')   
                print()
        
        horizontal_line(dim_size)
    
        print(' ')
        print('Congratulations, YOU WIN!')


    def bomb_count(board, y, x)->int:
        value = 0
        if x < len(board)-1:
            if board[y][x+1] == 'B':
                value += 1
        if x > 0:
            if board[y][x-1] == 'B':
                value += 1
        if y < len(board)-1:
            if board[y+1][x] == 'B':
                value += 1
        if y > 0:
            if board[y-1][x] == 'B':
                value += 1
        if x < len(board)-1 and y < len(board)-1:
            if board[y+1][x+1] == 'B':
                value += 1
        if x > 0 and y < len(board)-1: 
            if board[y+1][x-1] == 'B':
                value += 1
        if x < len(board)-1 and y > 0:
            if board[y-1][x+1] == 'B':
                value += 1
        if x > 0 and y > 0:
            if board[y-1][x-1] == 'B':
                value += 1
        

        return value


    #this function draws a horizontal line using board dimention size
    def horizontal_line(length):
        for i in range(length):
            print('-----',end='')
        print()

    #this function add number on top of the board using its dimention size
    def X_axis_numbering(number):
        for col in range(number):
            if col != number:
                print('  {}  '.format(col),end='')
        print()

    #def adjacent_mine_count(_y_axis, _x_axis):
        #code to check adjacent mines


    #this is the program entry point
    user_answer = input('Welcome to minesweper, type "Y" to play or any key to quit: ').upper()

    if user_answer == 'Y':
        replay = 'Y'
        while replay == 'Y':
            size = int(input('enter board size (one side of the board): '))
            while size < 4 or size > 10:
                size = int(input('minimum size is 4, maximum size is 10. enter board size: '))
            bombs = int(input('enter number of bombes: '))
            if bombs > size or bombs == 0:
                while bombs > size or bombs == 0:
                    print(' ')
                    print('> bombs must be equal or be less than the board size!')
                    print('> you must enter atleast 1 bomb!')
                    bombs = int(input('enter number of bombes: '))
                
            #call play fnction to start game
            play(size, bombs)
            replay = input('Do you want to play again (Y/N): ').upper()
    
        
    print(' ')
    print('GOOD BYE!')
except:
    print('error, number required!')
    
