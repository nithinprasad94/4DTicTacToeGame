class board(object):

    def __init__(self,dim,filler):
        self.n = dim
        self.board_elems = []
        for j in range(self.n):
            row = []
            for i in range(self.n):
                row.append(str(filler))
            self.board_elems.append(row)            

    def return_row(self,row): #Prints a line
        print_string = ''
        for i in range(self.n):
            print_string += str(self.board_elems[row][i])
            print_string += ' '
        return print_string

#Test board
            
class grid(object):

    def __init__(self,rows,cols,board_size):
        self.num_rows = rows
        self.num_cols = cols
        self.grid_boards = []

        filler = '_'
        for r in range(self.num_rows):
            temp_row = []
            for c in range(self.num_cols):
                temp_board = None
                temp_board = board(board_size,filler)
                temp_row.append(temp_board)
            self.grid_boards.append(temp_row)

        
def print_grid(t3_grid,height,width):
    board_size = t3_grid.grid_boards[0][0].n
    for h in range(height):
        for y in range(board_size):
            grid_row = ''
            for w in range(width):
                grid_row += t3_grid.grid_boards[h][w].return_row(y)
                grid_row += '  '
            print(grid_row)
        print('')

def check_win(t3_grid,marker):
    board_size = t3_grid.grid_boards[0][0].n
    height = len(t3_grid.grid_boards)
    width = len(t3_grid.grid_boards[0])
    
    #Check for a win across the same board
    for i in range(height): 
        for j in range(width): #Now indexes a particular board ...
            temp_b = t3_grid.grid_boards[i][j].board_elems

            #Check for row equality
            for y in range(board_size):
                counter = 0
                for x in range(board_size):
                    if temp_b[y][x] == marker:
                        counter += 1
                if counter == board_size:
                    return True                

            #Check for column equality
            for x in range(board_size):
                counter = 0
                for y in range(board_size):
                    if temp_b[y][x] == marker:
                        counter += 1
                if counter == board_size:
                    return True

            #Check for diagonal equality
            counter = 0
            for k in range(board_size):
                if temp_b[k][k] == marker:
                    counter += 1
            if counter == board_size:
                #print("for real?")
                return True
            
            counter = 0
            for k in range(board_size):
                if temp_b[k][board_size-1-k] == marker:
                    counter += 1
            if counter == board_size:
                #print("huh?")
                return True

    print("Reaching checkpoint")

    #Check for win across row of boards
    for i in range(height):
        #Now indexing a particular row of boards ...

        #Check same row, same col, different w for row of boards
        for x in range(board_size):
    
            for y in range(board_size):

                counter = 0
                for j in range(width):
                    temp_b = t3_grid.grid_boards[i][j].board_elems
                    if temp_b[y][x] == marker:
                        counter += 1
                if counter == board_size:
                    return True        

        #Check same row, diff col, diff w for row of boards
        for y in range(board_size):
            counter = 0
            for j in range(width):
                temp_b = t3_grid.grid_boards[i][j].board_elems
                if temp_b[y][j] == marker:
                    counter += 1
            if counter == board_size:
                return True

        #Check diff row, same col, diff w for row of boards
        for x in range(board_size):
            counter = 0
            for j in range(width):
                temp_b = t3_grid.grid_boards[i][j].board_elems
                if temp_b[i][x] == marker:
                    counter += 1
            if counter == board_size:
                return True

        #print("mistake?")
        #Check diagonal(s) row,col, diff w for row of boards
        (counter,counter2,counter3,counter4) = (0,0,0,0)
        for k in range(board_size):
            temp_b = t3_grid.grid_boards[i][k].board_elems
            if temp_b[k][k] == marker:
                counter += 1
            if temp_b[k][board_size-1-k] == marker:
                counter2 += 1
            if temp_b[board_size-1-k][k] == marker:
                counter3 += 1
            if temp_b[board_size-1-k][board_size-1-k] == marker:
                counter4 += 1
        if counter == board_size or counter2 == board_size or counter3 == board_size or counter4 == board_size:
            return True


    print("Reaching second checkpoint ...")
    
    #Check for win across column of boards
    for j in range(width):
        #Now indexing a particular column of boards ...

        #Check same row, same col, different h for col of boards
        for x in range(board_size):
    
            for y in range(board_size):

                counter = 0
                for i in range(height):
                    temp_b = t3_grid.grid_boards[i][j].board_elems
                    if temp_b[y][x] == marker:
                        counter += 1
                if counter == board_size:
                    return True
                
        #Check same row, diff col, diff h for col of boards
        for y in range(board_size):
            counter = 0
            for i in range(height):
                temp_b = t3_grid.grid_boards[i][j].board_elems
                if temp_b[y][i] == marker:
                    counter += 1
            if counter == board_size:
                return True

        #Check diff row, same col, diff h for col of boards
        for x in range(board_size):
            counter = 0
            for i in range(height):
                temp_b = t3_grid.grid_boards[i][j].board_elems
                if temp_b[i][x] == marker:
                    counter += 1
            if counter == board_size:
                return True

        #Check diagonal row,col, diff w for row of boards
        (counter,counter2,counter3,counter4) = (0,0,0,0)
        for k in range(board_size):
            temp_b = t3_grid.grid_boards[k][j].board_elems
            if temp_b[k][k] == marker:
                counter += 1
            if temp_b[k][board_size-1-k] == marker:
                counter2 += 1
            if temp_b[board_size-1-k][k] == marker:
                counter3 += 1
            if temp_b[board_size-1-k][board_size-1-k] == marker:
                counter4 += 1
        if counter == board_size or counter2 == board_size or counter3 == board_size or counter4 == board_size:
            return True
    print("Reaching third checkpoint ...")    

    #Check for win across diagonal of boards

    (counter,counter2,counter3,counter4) = (0,0,0,0)
    for i in range(width):
        temp_b = t3_grid.grid_boards[i][i].board_elems

        if temp_b[i][i] == marker:
            counter += 1
        if temp_b[i][board_size-1-i] == marker:
            counter2 += 1
        if temp_b[board_size-1-i][i] == marker:
            counter3 += 1
        if temp_b[board_size-1-i][board_size-1-i] == marker:
            counter4 += 1
    if counter == board_size or counter2 == board_size or counter3 == board_size or counter4 == board_size:
        return True

    (counter,counter2,counter3,counter4) = (0,0,0,0)
    for i in range(width):
        temp_b = t3_grid.grid_boards[i][width-1-i].board_elems
        
        if temp_b[i][i] == marker:
            counter += 1
        if temp_b[i][board_size-1-i] == marker:
            counter2 += 1
        if temp_b[board_size-1-i][i] == marker:
            counter3 += 1
        if temp_b[board_size-1-i][board_size-1-i] == marker:
            counter4 += 1
    if counter == board_size or counter2 == board_size or counter3 == board_size or counter4 == board_size:
        return True
    
    #Otherwise, exhausting all win conditions ...
    return False
    
#Main program

#0) Ask User about board parameters
print("This game is called 4-D Tic-Tac-Toe")

valid_dim = False
while not(valid_dim):
    dim = input("Input dimension N for an NxNxNxN board between 3 and 5: ")
    dim = int(dim)
    if dim < 3 or dim > 5:
        print("Inadmissable value for dim. Please try again!")
    else:
        valid_dim = True
    
width = dim
height = dim

#Allow for multiple rounds of the game
play_again = True

while play_again:

    #1) Initialize Boards and Win Status
    t3_grid = grid(int(height),int(width),dim)
    #sample_board = t3_grid.grid_boards[0][0]
    #for m in range(5):
    #    sample_board.print_row(m)
    player_1_win = False
    player_2_win = False

    next_player = 1 #Initialize the next player to 1
    prev_coords = 0 #Initialize previous move's coords to be 0
    prev_player = 0

    #While loop to iterate through player moves
    while (not(player_1_win) and not(player_2_win)):              
        
        #2) Accept Player 1 Move (X)
        if (next_player == 1):
            #Print Grid
            print_grid(t3_grid,height,width) 
            
            print("Player 1 Move:")
            valid_move = False
            while not(valid_move):
                params = input("Please enter the w,h,x,y parameters: ")
                if (len(params) == 4):
                    if params != "undo":
                        (w,h,x,y) = params
                        w = int(w)
                        h = int(h)
                        x = int(x)
                        y = int(y)
                        temp_board = t3_grid.grid_boards[h][w]
                        if ((w > dim-1) or (w < 0)) or ((h > dim-1) or (h < 0)) or ((x > dim-1)
                            or (x < 0)) or ((y > dim-1) or (y < 0)):
                            print("At least one dimension entered is inadmissable!")
                        else:            
                            if temp_board.board_elems[y][x] != 'X' and temp_board.board_elems[y][x] != 'O':
                                valid_move = True
                            else:
                                print("Move was invalid because that location is already filled")
                    else:
                        valid_move = True
                else:
                    print("Wrong number of parameters!")
            if (params == "undo"):
                prev_p = prev_coords
                (w,h,x,y) = prev_p
                w = int(w)
                h = int(h)
                x = int(x)
                y = int(y)
                temp_board = t3_grid.grid_boards[h][w]
                temp_board.board_elems[y][x] = '_'

                next_player = 2
                prev_coords = 0
                prev_player = 1

            else:
                temp_board = t3_grid.grid_boards[h][w]
                temp_board.board_elems[y][x] = 'X'

                next_player = 2
                prev_coords = params
                prev_player = 1

                #3) Check for Win Condition
                player_1_win = check_win(t3_grid,'X')

                #Intermediate win-condition check
                if player_1_win:
                    break

        #4) Accept Player 2 Move (O)
        if (next_player == 2):
            #Print Grid
            print_grid(t3_grid,height,width)  
            
            print("Player 2 Move:")
            valid_move = False
            while not(valid_move):
                params = input("Please enter the w,h,x,y parameters: ")
                if (len(params) == 4):
                    if params != "undo":
                        (w,h,x,y) = params
                        w = int(w)
                        h = int(h)
                        x = int(x)
                        y = int(y)
                        temp_board = t3_grid.grid_boards[h][w]
                        if ((w > dim-1) or (w < 0)) or ((h > dim-1) or (h < 0)) or ((x > dim-1)
                            or (x < 0)) or ((y > dim-1) or (y < 0)):
                            print("At least one dimension entered is inadmissable!")
                        else:            
                            if temp_board.board_elems[y][x] != 'X' and temp_board.board_elems[y][x] != 'O':
                                valid_move = True
                            else:
                                print("Move was invalid because that location is already filled")
                    else:
                        valid_move = True
                else:
                    print("Wrong number of parameters!")

            if (params == "undo"):
                prev_p = prev_coords
                (w,h,x,y) = prev_p
                w = int(w)
                h = int(h)
                x = int(x)
                y = int(y)
                temp_board = t3_grid.grid_boards[h][w]
                temp_board.board_elems[y][x] = '_'

                next_player = 1
                prev_coords = 0
                prev_player = 2

            else:
                
                temp_board = t3_grid.grid_boards[h][w]
                temp_board.board_elems[y][x] = 'O'

                next_player = 1
                prev_coords = params
                prev_player = 2
                
                #5) Check for Win Condition
                player_2_win = check_win(t3_grid,'O')

    #6) Announce Results
    print("Final grid: ")
    print_grid(t3_grid,height,width)
    if player_1_win:
        print("Player 1 has won!")
    elif player_2_win:
        print("Player 2 has won!")

    valid_choice = False
    while not(valid_choice):
        choice = input("Would you like to play again (y/n)? ")
        if choice == 'y' or choice == 'n':
            valid_choice = True
    if choice == 'n':
        play_again = False

print("Thanks for playing!")
    
    
    
