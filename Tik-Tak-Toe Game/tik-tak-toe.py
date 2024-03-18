possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of numbers for the game
gameBoard = [[1, 2, 3],  # array representing the game board
             [4, 5, 6],
             [7, 8, 9]]
rows = 3  # Number of rows in the game board
cols = 3  # Number of columns in the game board


def print_game_board():
    """
    Prints the game board.
    """
    for x in range(rows):
        print("\n|---|---|---|")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n|---|---|---|")


def modify_array(num, turn):
    """
    Updates the game board with the player's move.

    Parameters:
    num (int): The number corresponding to the cell to be marked.
    turn (str): The player's mark ('X' or 'O').
    """
    num -= 1  # Adjust for 0-index
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn


def check_for_winner(game_board):
    """
    Checks for a winner or a tie by analyzing the game board.

    Returns:
    str or None: The winning player's mark ('X' or 'O') if there is a winner, or None if there is a tie.
    """
    # Rows
    for row in game_board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Columns
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col]:
            return game_board[0][col]

    # Cross
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return game_board[0][2]

    return None


leaveLoop = False
turnCounter = 0  # check who play first

while not leaveLoop:
    print_game_board()

    if turnCounter % 2 == 0:
        player = 'X'
    else:
        player = 'O'

    numberPicked = int(input(f"\nPlayer '{player}', please choose a number [1-9]: "))

    if numberPicked in possibleNumbers:
        modify_array(numberPicked, player)
        possibleNumbers.remove(numberPicked)
        winner = check_for_winner(gameBoard)
        if winner:
            print_game_board()
            print(f"\nPlayer '{winner}' wins!")
            leaveLoop = True
        elif len(possibleNumbers) == 0:
            print_game_board()
            print("\nThe game ends in a tie!")
            leaveLoop = True
        else:
            turnCounter += 1
    else:
        print("Invalid input. Try again")
