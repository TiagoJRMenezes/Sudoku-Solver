from main import *

def menu():
    flag = 1

    print("1 - Insert your sudoku problem")
    print("2 - Use already set up example")
    print("3 - Terminate program")
    option = input("Which option do you want to choose: ")

    while flag == 1:

        if option == "1":
            flag = 0
            menu_option1()
            break

        if option == "2":
            flag = 0
            menu_option2()
            break

        if option == "3":
            break

        else:
            option = input("That option is not valid. Insert a valid number: ")

    print("Thank you for using this solver")








def menu_option1():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Insert your problem in the following format")
    print("A B C D E F G H I (Insert the empty spaces as zeros")

    for i in range(9):
        row = input()
        spl = row.split( )
        for j in range(len(spl)):
            temporary = int(spl[j])
            set_board_number(board,temporary,i,j)

    print("\nDone inserting the board")
    solver(board)
    print("\n    Solved Version \n")
    print_board(board)
    print("\n")

    return

def menu_option2():
    return


menu()