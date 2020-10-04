# Function to print Board
def tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Function to print the score-board
def scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCORE BOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Function to check if any player has won
def check_win(player_pos, player):
 
    # All possible winning combinations
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in win:
        if all(y in player_pos[player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a game of Tic Tac Toe
def game(player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("It\'s Player ", player, " turn. Enter box no.? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Try Again!!")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print(" move should be b/w 1 and 9")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place is already filled. Choose another.")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = player
 
        # Updating player positions
        player_pos[player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, player):
            tic_tac_toe(values)
            print("Congrats! Player ", player, " has won the game!!")     
            print("\n")
            return player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            tic_tac_toe(values)
            print("Oh! The Game is tie! Better luck next time!")
            print("\n")
            return 'D'
 
        # Switch player moves
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
 
if __name__ == "__main__":
    print("Welcome to TIC-TAC-TOE Game!\n")
    print("Player 1")
    player1 = input("Enter your name : ")
    
 
    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")
     
    # Stores the player who chooses X and O
    player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", player)
        print("Enter 1 if you want to be X")
        print("Enter 2 if you want to be O")
        print("Enter 3 to Quit the game")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print("Check the Input!!! \n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = player
            if player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = player
            if player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Try Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        scoreboard(score_board)
        # Switch player who chooses X or O
        if player == player1:
            player = player2
        else:
            player = player1
