# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
    # Show the initial game board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:
        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X":
        print("Computer won.")
    elif winner == "O":
        print("User won.")
    elif winner == None:
        print("Tie.")


# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    if player == "X":
        computer()
    elif player == "O":
        user()


def user():
    global board
    # Get position from player
    print("O's turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = "O"

    # Show the game board
    display_board()

def computer():
    global board
    print("X's turn.")
    # Get open corner
    emptyCorners = getEmptyCorners()
    # Get open edge
    emptyEdges = getEmptyEdges()

    # Check for third square to win
    # Rows
    if board[0] == board[1] == "X" and board[2] == "-":
        board[2] = "X"
    elif board[0] == board[2] == "X" and board[1] == "-":
        board[1] = "X"
    elif board[1] == board[2] == "X" and board[0] == "-":
        board[0] = "X"

    elif board[3] == board[4] == "X" and board[5] == "-":
        board[5] = "X"
    elif board[3] == board[5] == "X" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[5] == "X" and board[3] == "-":
        board[3] = "X"

    elif board[6] == board[7] == "X" and board[8] == "-":
        board[8] = "X"
    elif board[6] == board[8] == "X" and board[7] == "-":
        board[7] = "X"
    elif board[7] == board[8] == "X" and board[6] == "-":
        board[6] = "X"


    # Columns
    elif board[0] == board[3] == "X" and board[6] == "-":
        board[6] = "X"
    elif board[0] == board[6] == "X" and board[3] == "-":
        board[3] = "X"
    elif board[3] == board[6] == "X" and board[0] == "-":
        board[0] = "X"

    elif board[1] == board[4] == "X" and board[7] == "-":
        board[7] = "X"
    elif board[1] == board[7] == "X" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[7] == "X" and board[1] == "-":
        board[1] = "X"

    elif board[2] == board[5] == "X" and board[8] == "-":
        board[8] = "X"
    elif board[2] == board[8] == "X" and board[5] == "-":
        board[5] = "X"
    elif board[5] == board[8] == "X" and board[2] == "-":
        board[2] = "X"

    # Diagonals
    elif board[0] == board[4] == "X" and board[8] == "-":
        board[8] = "X"
    elif board[0] == board[8] == "X" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[8] == "X" and board[0] == "-":
        board[0] = "X"

    elif board[2] == board[4] == "X" and board[6] == "-":
        board[6] = "X"
    elif board[2] == board[6] == "X" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[6] == "X" and board[2] == "-":
        board[2] = "X"



    # Check third square to block opponent
    # Rows
    elif board[0] == board[1] == "O" and board[2] == "-":
        board[2] = "X"
    elif board[0] == board[2] == "O" and board[1] == "-":
        board[1] = "X"
    elif board[1] == board[2] == "O" and board[0] == "-":
        board[0] = "X"

    elif board[3] == board[4] == "O" and board[5] == "-":
        board[5] = "X"
    elif board[3] == board[5] == "O" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[5] == "O" and board[3] == "-":
        board[3] = "X"

    elif board[6] == board[7] == "O" and board[8] == "-":
        board[8] = "X"
    elif board[6] == board[8] == "O" and board[7] == "-":
        board[7] = "X"
    elif board[7] == board[8] == "O" and board[6] == "-":
        board[6] = "X"


    # Columns
    elif board[0] == board[3] == "O" and board[6] == "-":
        board[6] = "X"
    elif board[0] == board[6] == "O" and board[3] == "-":
        board[3] = "X"
    elif board[3] == board[6] == "O" and board[0] == "-":
        board[0] = "X"

    elif board[1] == board[4] == "O" and board[7] == "-":
        board[7] = "X"
    elif board[1] == board[7] == "O" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[7] == "O" and board[1] == "-":
        board[1] = "X"

    elif board[2] == board[5] == "O" and board[8] == "-":
        board[8] = "X"
    elif board[2] == board[8] == "O" and board[5] == "-":
        board[5] = "X"
    elif board[5] == board[8] == "O" and board[2] == "-":
        board[2] = "X"

    # Diagonals
    elif board[0] == board[4] == "O" and board[8] == "-":
        board[8] = "X"
    elif board[0] == board[8] == "O" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[8] == "O" and board[0] == "-":
        board[0] = "X"

    elif board[2] == board[4] == "O" and board[6] == "-":
        board[6] = "X"
    elif board[2] == board[6] == "O" and board[4] == "-":
        board[4] = "X"
    elif board[4] == board[6] == "O" and board[2] == "-":
        board[2] = "X"


    # Try to take one of the corners
    elif emptyCorners:
        board[randomSelection(emptyCorners)] = "X"

    # Try to take the center
    elif board[5] != "-":
        board[5] = "X"

    # Take any edge
    elif emptyEdges:
        board[randomSelection(emptyEdges)] = "X"

    # Show the game board
    display_board()

def getEmptyCorners():
    corners = [0, 2, 6, 8]
    fullCorner = []
    for corner in corners:
        if board[corner] == "X" or board[corner] == "O":
            fullCorner.append(corner)

    emptyCorner = [item for item in corners if item not in fullCorner]

    return emptyCorner

def getEmptyEdges():
    edges = [1, 3, 5, 7]
    fullEdge = []
    for edge in edges:
        if board[edge] == "X" or board[edge] == "O":
            fullEdge.append(edge)

    emptyEdge = [item for item in edges if item not in fullEdge]

    return emptyEdge

def randomSelection(list):
    import random
    n = len(list)
    r = random.randint(0, n - 1)
    return list[r]


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()