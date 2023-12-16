from random import randrange


def play_game():
    rows = cols = 3
    board = [[0 in range(cols)] in range(rows)]
    counter = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = counter
            counter += 1

    display_board(board)
    winner = (victory_for(board, "X") or victory_for(board, "0"))
    while (not winner) and not is_tie(board):
        winner = draw_move(board) or enter_move(board)
        if is_tie(board):
            print("This game ended in a tie. Try Again")


def display_board(board):
    row = col = 0
    for i in range(1, 13):
        print("+-------", end="")
        if i % 3 == 0:
            print("+")
            for j in range(1, 10):
                if i == 12:
                    break
                if 3 < j < 7:
                    print("|   " + str(board[row][col]) + "   ", end="")
                    col += 1
                else:
                    print("|       ", end="")
                if j % 3 == 0:
                    print("|")
            row += 1
            col = 0
    make_list_of_free_fields(board)


def enter_move(board):
    valid_move = 0
    while valid_move == 0 and not is_tie(board):
        move = int(input("Enter your move: "))
        if move < 0 or move >= 10:
            valid_move = 0
            print("Invalid move!")
        elif 0 < move < 4:
            if (0, move - 1) in make_list_of_free_fields(board):
                valid_move = move
                board[0][move - 1] = "0"
            else:
                valid_move = 0
                print("Invalid move!")
        elif 3 < move < 7:
            if (1, move - 4) in make_list_of_free_fields(board):
                valid_move = move
                board[1][move - 4] = "0"
            else:
                valid_move = 0
                print("Invalid move!")
        elif 6 < move < 10:
            valid_move = move
            if (2, move - 7) in make_list_of_free_fields(board):
                board[2][move - 7] = "0"
            else:
                valid_move = 0
                print("Invalid move!")

    if is_tie(board):
        return

    make_list_of_free_fields(board)
    display_board(board)
    return victory_for(board, "0")


def make_list_of_free_fields(board):
    available_field = ()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "0":
                available_field += ((i, j),)
    return available_field


def draw_move(board):
    print("Computer's Move")
    comp_move = 5
    while comp_move != 0 and not is_tie(board):
        if 0 < comp_move < 4:
            if (0, comp_move - 1) in make_list_of_free_fields(board):
                board[0][comp_move - 1] = "X"
                comp_move = 0
            else:
                comp_move = randrange(1, 10)
        elif 3 < comp_move < 7:
            if (1, comp_move - 4) in make_list_of_free_fields(board):
                board[1][comp_move - 4] = "X"
                comp_move = 0
            else:
                comp_move = randrange(1, 10)
        elif 6 < comp_move < 10:
            if (2, comp_move - 7) in make_list_of_free_fields(board):
                board[2][comp_move - 7] = "X"
                comp_move = 0
            else:
                comp_move = randrange(1, 10)

    make_list_of_free_fields(board)
    display_board(board)
    if is_tie(board):
        return
    return victory_for(board, "X")


def victory_for(board, sign):
    victory = False
    # rows
    if board[0][0] == board[0][1] == board[0][2] == sign:
        victory = True
    elif board[1][0] == board[1][1] == board[1][2] == sign:
        victory = True
    elif board[2][0] == board[2][1] == board[2][2] == sign:
        victory = True
    # columns
    elif board[0][0] == board[1][0] == board[2][0] == sign:
        victory = True
    elif board[0][1] == board[1][1] == board[2][1] == sign:
        victory = True
    elif board[0][2] == board[1][2] == board[2][2] == sign:
        victory = True

    # diagonals
    elif board[0][0] == board[1][1] == board[2][2] == sign:
        victory = True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        victory = True

    if victory and sign == "X":
        print("Computer Wins, Try again")
    elif victory and sign == "0":
        print("You Win!!!!")
    return victory


def is_tie(board):
    if len(make_list_of_free_fields(board)) == 0:
        return True
    else:
        return False


play_game()
