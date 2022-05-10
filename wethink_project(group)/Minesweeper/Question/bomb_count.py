board = [[0,0,0,0],
        [0,0,0,0],
         [0,0,0,0],
         ['B',0,0,'B']]

y = 1
x= 0

value = 0

if x < len(board)-1:
    if board[y][x+1] == 'B':
        value+=1  
if board[y][x-1] == 'B':
        value+=1
if y < len(board)-1:
    if board[y+1][x] == 'B':
        value+=1
if y < 0:
        if board[y-1][x] == 'B':
                value+=1
if y < len(board)-1 and x < len(board)-1:
    if board[y+1][x+1] == 'B':
        value+=1
if y < len(board)-1:
    if board[y+1][x-1] == 'B':
        value+=1
if x < len(board)-1:
        if y < 0:
                if board[y-1][x+1] == 'B':
                        value+=1
if y < 0:
        if board[y-1][x-1] == 'B':
                value+=1  


                     
print(value)


                    
                        
                        
 
                
                    
                    
                      