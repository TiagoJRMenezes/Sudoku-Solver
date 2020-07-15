"""
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
"""
#Finds the first empty space in the board

def find_space(board):

    for i in range(len(board)): #check every row
        for j in range(len(board[0])): #check every column of that row
            if board[i][j] == 0: #if space empty
                return (i, j) #returns row and col

    return None #returns None if there is no empty space

#Validates the number to input in the empty space

def validate(board, number, row, col):

    for i in range(len(board)):  # Check the every column of the row the number is in for equal numbers
        if board[row][i] == number and col != i:  # Equal number and not the same column where the number is
            return False

    for i in range(len(board)):  # Check the every row of the column the number is in for equal numbers
        if board[i][col] == number and row != i:  # Equal number and not the same row where the number is
            return False


    box_row = row // 3  # Defines which box (1,2 or 3) of the boxes in the axis of y the number is inserted in
    box_col = col // 3  # Defines which box (1,2 or 3) of the boxes in the axis of x the number is inserted in


    for i in range(box_row*3, box_row*3 +3):  #Starts in the first number of the box until the last one in the boxes in the y axis
        for j in range(box_col*3, box_col*3 + 3):  #Starts in the first number of the box until the last on in the boxes in the x axis
            if board[i][j] == number and (i,j) != (row,col):
                return False;

    return True;


#Function to print the board

def print_board(board):
    for i in range(len(board)): #pass every row
        if i % 3 == 0 and i != 0: #if it's the third row print the line
            print("- - - - - - - - - - - - - ")

        for j in range(len(board)): #pass every column of that row
            if j % 3 == 0 and j != 0: # if it's the third column print the line (end="" so it doesnt print a /n)
                print(" | ", end="")

            if j == 8: #print the last column of that row (needs it's seperate if since the else condition doesn't print a /n)
                print(board[i][j])

            else: #print evey number (number converted to string to add the space
                print(str(board[i][j]) + " ", end="")


#Backtracking algorithm to solve the sudoku board

def solver(board):
    space = find_space(board)  #Finds the empty space

    if not space:  #If it can't find it, it ends
        return True

    else:
        row,col = space; #Sets the value for row and column of the empty space found

    for i in range(1,10):  #Tries for every number between 1 and 9
        if validate(board,i,row,col):  #If the number is valid
            set_board_number(board,i,row,col)  #Insert the number

            if solver(board):  #If True (that comes from not having any more spaces to find) it returns true since we found the solution
                return True

            else:  #In case that it doesnt return True, it means that it failed the solution so it resets the most recent change to the board
                set_board_number(board,0,row,col)

    return False


#Changes the number in the board for a certain row and column
def set_board_number(board, number, row, col):
    board[row][col] = number
    return


